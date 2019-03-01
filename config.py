import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
  DEBUG = False
  TESTING = False
  CSRF_ENABLED = True
  SECRET_KEY = 'thisissecret'

class DevelopmentConfig(Config):
  DEVELOPMENT = True
  DEBUG = True
  BASE_URL = 'http://localhost:5000/'
  # MongoDB
  MONGODB_DB = 'Locus'
  MONGODB_HOST = '127.0.0.1'
  MONGODB_PORT = 27017
  MONGODB_USERNAME = 'admin'
  MONGODB_PASSWORD = 'password'


class ProductionConfig(Config):
  DEBUG = True
  DEVELOPMENT = True
  BASE_URL = ''
  # MongoDB
  MONGODB_DB = ''
  MONGODB_USERNAME = ''
  MONGODB_PASSWORD = ''
  MONGODB_HOST = ''