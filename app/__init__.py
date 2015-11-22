from flask import Flask
from flask.ext.bootstrap import Bootstrap
from flask.ext.moment import Moment
from redis import StrictRedis

app = Flask(__name__)
app.config.from_object('config')

bootstrap = Bootstrap(app)
moment = Moment(app)
redis = StrictRedis(decode_responses = True)

from app import views
