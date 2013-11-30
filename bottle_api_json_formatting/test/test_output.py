#!/usr/bin/env python
''' Test suite for bottle-api-json-formatting '''

#pylint: disable=W0403
from base import TestBase
import unittest
import json

class TestOutput(TestBase):
# pylint: disable=R0904
    ''' Test suite '''
    def test_standard_result(self):
        ''' Test for a standard response '''
        result = self.app.get('/')
        self.assertEqual(result.status_code, 200)
        data = json.loads(result.body)
        self.assertEqual(data['status_code'], 0)

    def test_error_result(self):
        ''' Test for a 401 error '''
        result = self.app.get('/error', expect_errors=True)
        self.assertEqual(result.status_code, 401)
        data = json.loads(result.body)
        self.assertEqual(data['status_code'], 1)

    def test_failure_result(self):
        ''' Test for a 500 error '''
        result = self.app.get('/failure', expect_errors=True)
        self.assertEqual(result.status_code, 500)
        data = json.loads(result.body)
        self.assertEqual(data['status_code'], 1)

    def test_uninstall(self):
        ''' Test that the plugin uninstalls correctly '''
        result = self.app.get('/uninstall')
        self.assertEqual(result.status_code, 200)
        result = self.app.get('/')
        self.assertEqual(result.status_code, 200)
        try:
            data = json.loads(result.body)
        except Exception as e:
            self.assertEqual(type(e), ValueError)

    def test_accept_media_types(self):
        ''' Test accept media types'''
        form_data = {'mediatypes': 'application/json'}
        result = self.app.post('/switchmediatypes', form_data)
        self.assertEqual(result.status_code, 200)
        result = self.app.get('/')
        self.assertEqual(result.body, 'test')
        headers = {'Accept': 'application/json'}
        result = self.app.get('/', headers=headers)
        data = json.loads(result.body)
        self.assertEqual(data['status_code'], 0)
        result = self.app.post('/switchmediatypes')
        self.assertEqual(result.status_code, 200)
        result = self.app.get('/')
        data = json.loads(result.body)
        self.assertEqual(data['status_code'], 0)

if __name__ == '__main__':
   unittest.main() 
