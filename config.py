import os
basedir = os.path.abspath(os.path.dirname(__file__))

 # General Config
WTF_CSRF_ENABLED = True
SECRET_KEY = os.environ.get('SECRET_KEY') or 'safdfsdgf'


# Database
SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL_') or \
        'sqlite:///' + os.path.join(basedir, 'site.db')

SQLALCHEMY_TRACK_MODIFICATIONS = False

