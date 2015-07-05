import os
__author__ = 'kavin'


TEMPLATE_DIRS = (

    (os.path.dirname(__file__).rsplit('/', 1)[0] + '/core_code/templates').replace('\\', '/'),
)
