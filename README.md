=====================
bottle-api-json-formatting
=====================

A Bottle plugin which encapsulates results and errors in a json object. This 
makes it much easier to build REST based api services with bottle. 


Installation
===============

Install with one of the following commands:
```bash
$ pip install bottle-api-json-formatting
$ easy_install bottle-api-json-formatting
```
or download the latest version from github:
```bash
$ git clone git://github.com/bustleandflurry/bottle-api-json-formatting.git
$ cd bottle-api-json-formatting
$ python setup.py install
```


Usage
===============
```python
import bottle
import bottle_api_json_formatting

app = bottle.Bottle()
app.install(bottle_api_json_formatting.JsonFormatting())

@app.route('/')
def index():
    return 'This is a test.'

@APP.route('/error')
def index():
    raise Exception('This is an error.')

if __name__ == '__main__':
    run(app, host='0.0.0.0', port=8080, debug=True)
```


Output
=============

Standard:
```
{
    "status": "success", 
    "status_code": 0, 
    "data": "test"
}
```

Error:
```
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
```


Module Contents
=============

bottle\_api\_json\_formatting.**JsonFormatting**(*supported\_types=*['\*/\*'], *debug=False*)

*supported\_types* allows you to expressly set which Content-Types are acceptable for a json formatted response. When set any Content-Types not in the will be passed through untouched. 

*debug* set to True will add the fields exception and traceback to error responses.


