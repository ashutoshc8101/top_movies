from flask import jsonify, Blueprint
from topmovies.db.models import movie

blueprint = Blueprint('top_movies', __name__)

@blueprint.route('/top_movies')
def top_movies():
    data = movie.Movie.query.all()
    return jsonify(data)