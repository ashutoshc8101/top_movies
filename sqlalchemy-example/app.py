from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
app = Flask(__name__)

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:@localhost/alchemy'

db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    date_created = db.Column(db.DateTime, default=datetime.now)
    def __repr__(self):
        return '<User %r>' % self.username

@app.route('/create_user/<username>/<email>/')
def home(username, email):
    user = User(username=username, email=email)
    db.session.add(user)
    db.session.commit()
    return 'User created'

@app.route('/get_user/<username>')
def getUser(username):
    user = User.query.filter_by(username=username).first()
    return user.email

if __name__ == '__main__':
    app.run(debug=True)
