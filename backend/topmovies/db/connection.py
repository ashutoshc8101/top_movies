from flask_sqlalchemy import SQLAlchemy

from topmovies import app

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:@127.0.0.1/top_movies' 

db = SQLAlchemy(app)