# import os

from flask import Flask
from flask import render_template
from flask import session, request, make_response, jsonify
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['DATABASE_URL']
app.config['SQLALCHEMY_DATABASE_URI'] = "postgres://sllynvkpwzcmnr:5QO8q__RWGhpNEowuVYs-OEXBZ@ec2-54-225-101-64.compute-1.amazonaws.com:5432/dblnmi4smbffiv"
db = SQLAlchemy(app)




####### Database classes/schema

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String(80))
    lastname = db.Column(db.String(80))
    email = db.Column(db.String(120), unique=True)

    def __init__(self, firstname, lastname, email):
        self.firstname = firstname
        self.lastname = firstname
        self.email = email

    def __repr__(self):
        return '<Name %r>' % self.name


class Poem(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255))
    body = db.Column(db.Text)

    def __init__(self, fi, email):
        self.title = title
        self.body = body

    def __repr__(self):
        return '<Name %r>' % self.name




########  Routing

@app.route('/')
def home():
    all_users = User.query.all()
    app.logger.debug( all_users)
    return render_template('index.html')


@app.route('/adduser' , methods=['POST'])
def add_user():
    user_info=request.form
    app.logger.debug(user_info)
    user = User(user_info['firstname'], user_info['lastname'], user_info['email'])
    #query database for unique email

    #if not unique: resp = make_response(jsonify(success=False))

    #if user is new add it
    db.session.add(user)
    db.session.commit()
    resp = make_response(jsonify(success=True))
    return resp


@app.route('/profile/<name>')
def profile(name):
    return render_template('profile.html',name=name)


@app.route('/signup')
def signup():
    return render_template('signup.html')


@app.route('/robots.txt')
def robots():
    res = app.make_response('User-agent: *\nAllow: /')
    res.mimetype = 'text/plain'
    return res





if __name__ == '__main__':
    app.run(debug=True)

