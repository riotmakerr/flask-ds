from creds import DATABASE_URI, CONFIG_SECRET_KEY

SQLALCHEMY_DATABASE_URI = DATABASE_URI
SQLALCHEMY_TRACK_MODIFICATIONS = false
SQLALCHEMY_POOL_RECYCLE = 3600

WTF_CSRF_ENABLED = True

SECRET_KEY = CONFIG_SECRET_KEY
