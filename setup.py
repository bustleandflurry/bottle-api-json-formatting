import os
from setuptools import setup

# Utility function to read the README file.
# Used for the long_description.  It's nice, because now 1) we have a top level
# README file and 2) it's easier to type in the README file than to put a raw
# string in below ...
def read(fname):
	return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
	name = "bottle-api-json-formatting",
    packages = ['bottle_api_json_formatting',],
	version = "0.0.5",
	author = "Aron Bartling",
	author_email = "aron@bustleandflurry.com",
	description = ("A bottle plugin to json format standard and error responses. \
        Intended for REST APIs."),
	license = "MIT",
	keywords = "Bottle Plugin JSON",
	url = "http://www.bustleandflurry.com",
	long_description = read('README.md'),
	classifiers = [
		"Development Status :: 3 - Alpha",
		"Topic :: Internet",
        "Environment :: Plugins",
        "Framework :: Bottle",
		"License :: OSI Approved :: MIT License",
        "Intended Audience :: Developers",
	],
    install_requires = ['bottle>=0.11'],
    test_suite = 'bottle_api_json_formatting'
)
