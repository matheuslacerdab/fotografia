import os
baseDir = os.path.abspath(os.path.dirname(__file__))

DEBUG = True
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(baseDir, 'database.db')
SQLALCHEMY_TRACK_MODIFICATIONS = True
SECRET_KEY = 'chave'