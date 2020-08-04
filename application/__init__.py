from flask import Flask
# from config import Config
# from flask_mongoengine import MongoEngine

app = Flask(__name__) #gets imported into main
# app.config.from_object(Config)

# db = MongoEngine()
# db.init__app(app)
from application import routes
