from topmovies.db.connection import db
class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(25), nullable=False)
    director = db.Column(db.String(25), nullable=False)
    cast = db.Column(db.String(25), nullable=False)
    imdb = db.Column(db.String(5), nullable=False)

    def __repr__(self):
        return f'{self.id}, {self.name}, {self.director}, {self.cast}, {self.imdb}'
