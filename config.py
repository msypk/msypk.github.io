import os

class Config(object):

    SECRET_KEY = os.environ.get('SECRET_KEY') or "redbluevioletflowerplant" #signature key to ensure that anything u send accross the server hasn't been hacked
    MONGODB_SETTINGS = { 'db' : 'Personal'}