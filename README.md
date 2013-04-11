=====================
bottle-api-json-formatting
=====================

A Bottle plugin which encapsulates results and errors in a json object. This 
makes it much easier to build REST based api services with bottle. 


Installation
===============

Install with one of the following commands::

    $ pip install bottle-api-json-formatting
    $ easy_install bottle-api-json-formatting

or download the latest version from github::

    $ git clone git://github.com/bustleandflurry/bottle-api-json-formatting.git
    $ cd bottle-api-json-formatting
    $ python setup.py install


Usage
===============

import bottle
import bottle-api-json-formatting

app = bottle.Bottle()
app.install(bottle_api_json_formatting.json_formatting())

@app.route('/')
def index():
    return 'This is a test.'

@APP.route('/error')
def index():
    raise Exception('This is an error.')

if __name__ == '__main__':
    run(app, host='0.0.0.0', port=8080, debug=True)


Output
=============

Standard:
{
    "status": "success", 
    "status_code": 0, 
    "data": "test"
}

Error:
{
    "status": "error", 
    "status_code": 1, 
    "data": null, 
    "error": {
        "status": "500 Internal Server Error", 
        "status_code": 500, 
        "message": "Internal Server Error"
    }
}



Configuration
=============

bottle_api_json_formatting.json_formatting(debug=True)
