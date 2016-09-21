import os 

#let's get that folder where our script lives
basedir = os.path.abspath(os.path.dirname(__file__))

DATABASE = 'flasktaskr.db'
CSRF_ENABLED = True
SECRET_KEY = 'ablaidjdbycajdibnryeeb'

#let's define the full path for the DATABASE
DATABASE_PATH = os.path.join(basedir, DATABASE)

SQLALCHEMY_DATABASE_URI = "sqlite:///" + DATABASE_PATH