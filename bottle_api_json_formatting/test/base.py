#!/usr/bin/env python
''' Test suite for bottle-api-json-formatting '''

import unittest
from webtest import TestApp

class TestBase(unittest.TestCase):
# pylint: disable=R0904
    ''' Test suite '''
    # pylint: disable=C0103
    def setUp(self):
        ''' Setup webtest '''
        import sys
        from ..test_app import APP
        self.app = TestApp(APP)

def _setup_logging():
    ''' Convenience setup for logging '''
    import logging
    logger = logging.getLogger('')
    logger.setLevel(logging.DEBUG)
    stream_handler = logging.StreamHandler(sys.stdout)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - \
            %(message)s')
    stream_handler.setFormatter(formatter)
    logger.addHandler(stream_handler)
    logger.info('Logging Enabled')
    logger.debug('DEBUG Enabled')


if __name__ == '__main__':
    import sys
    #sys.path = ['../bottle-api-authentication'] + sys.path
    _setup_logging()
    unittest.main()
