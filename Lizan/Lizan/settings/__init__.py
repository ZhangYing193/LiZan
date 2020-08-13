from pymysql import install_as_MySQLdb

install_as_MySQLdb()
#     raise ImproperlyConfigured('mysqlclient 1.4.0 or newer is required; you have %s.' % Database.__version__)
# django.core.exceptions.ImproperlyConfigured: mysqlclient 1.4.0 or newer is required; you have 0.10.0.

import pymysql
pymysql.version_info = (1, 4, 13, 'final', 0)
pymysql.install_as_MySQLdb()