from flask import Flask
from topmovies.routes import movie
app = Flask(__name__)
app.register_blueprint(movie.blueprint)