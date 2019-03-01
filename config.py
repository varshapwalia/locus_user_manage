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
  BASE_URL = ' https://locus-test.herokuapp.com/'
  # MongoDB
  MONGODB_DB = 'Locus'
  MONGODB_USERNAME = 'test'
  MONGODB_PASSWORD = 'Password.1'
  MONGODB_HOST = 'mongodb://cluster0-shard-00-00-iyb6j.mongodb.net:27017,cluster0-shard-00-01-iyb6j.mongodb.net:27017,cluster0-shard-00-02-iyb6j.mongodb.net:27017/test?ssl=true&replicaSet=Cluster0-shard-0&authSource=admin&retryWrites=true'