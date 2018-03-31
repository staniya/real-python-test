import os

# grab the folder where this script lives
basedir = os.path.abspath(os.path.dirname(__file__))

DATABASE = 'flasktaskr.db'
USERNAME = 'admin'
PASSWORD = 'admin'
WTF_CSRF_ENABLED = True
SECRET_KEY = ']\x8e\xfb++:[\xad\xefe\xc1q\xe1U\x1e\xff1\xbd\xb1S\xc1C\x0c\xbf'

# define the full path for the database
DATABASE_PATH = os.path.join(basedir, DATABASE)
