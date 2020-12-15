import os

SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'postgresql://booklovers:d3r_pAr0l@localhost/booklovers'
SQLALCHEMY_TRACK_MODIFICATIONS = False

FLASK_ENV = 'development'
FLASK_DEBUG = True