''' Formats output in a json schema. To be used for making json based API 
servers '''

from bottle import Bottle, response

# Co-opted the Bottle json import strategy
try:
    #pylint: disable=F0401 
    from json import dumps as json_dumps
except ImportError: # pragma: no cover
    try: 
        #pylint: disable=F0401 
        from simplejson import dumps as json_dumps
    except ImportError:
        try: 
            #pylint: disable=F0401
            from django.utils.simplejson import dumps as json_dumps
        except ImportError:
            #pylint: disable=W0613
            def json_dumps(data):
                ''' Place holder for lack of appropriate json lib '''
                raise ImportError(
                    'JSON support requires Python 2.6 or simplejson.')


class JsonFormatting(object):
    ''' Bottle plugin which encapsulates results and error in a json object. 
    Intended for instances where you want to use Bottle as an api server. '''

    name = 'json_formatting'
    api = 2

    statuses = {
            0: 'success',
            1: 'error',
            2: 'internal failure',
        }

    def __init__(self, debug=False):
        self.debug = debug
        self.app = None
        self.function_type = None
        self.function_original = None

    def setup(self, app):
        ''' Handle plugin install '''
        self.app = app
        self.function_type = type(app.default_error_handler)
        self.function_original = app.default_error_handler
        self.app.default_error_handler = self.function_type(
                self.custom_error_handler, app, Bottle)

    #pylint: disable=W0613
    def apply(self, callback, route):
        ''' Handle route callbacks '''
        if not json_dumps: 
            return callback
        def wrapper(*a, **ka):
            ''' Encapsulate the result in json '''
            output = callback(*a, **ka)
            response_object = self.get_response_object(0)
            response_object['data'] = output
            json_response = json_dumps(response_object)
            response.content_type = 'application/json'
            return json_response
        return wrapper

    def close(self):
        ''' Put the original function back on uninstall '''
        self.app.default_error_handler = self.function_type(
                self.function_original, self.app, Bottle)

    def get_response_object(self, status):
        ''' Helper for building the json object '''
        #global statuses
        if status in self.statuses:
            json_response = {
                    'status': self.statuses.get(status),
                    'status_code': status,
                    'data': None,
                }
            return json_response
        else:
            self.get_response_object(2)
        
    def custom_error_handler(self, res, error):
        ''' Monkey patch method for json formatting error responses '''
        response_object = self.get_response_object(1)
        response_object['error'] = {
                'status_code': error.status_code,
                'status': error.status_line,
                'message': error.body,
            }
        if self.debug:
            response_object['debug'] = {
                    'exception': error.exception,
                    'traceback': error.traceback,
                }
        json_response = json_dumps(response_object)
        response.content_type = 'application/json'
        return json_response
