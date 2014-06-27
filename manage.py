from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.script import Manager
from flask.ext.migrate import Migrate, MigrateCommand

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "postgres://sllynvkpwzcmnr:5QO8q__RWGhpNEowuVYs-OEXBZ@ec2-54-225-101-64.compute-1.amazonaws.com:5432/dblnmi4smbffiv"

db = SQLAlchemy(app)
migrate = Migrate(app, db)

manager = Manager(app)
manager.add_command('db', MigrateCommand)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String(80))
    lastname = db.Column(db.String(80))
    email = db.Column(db.String(120), unique=True)
    picture_url=db.Column(db.String(120))
    username=db.Column(db.String(80))

    def __init__(self, firstname, lastname, email, username, picture_url=None):
        self.firstname = firstname
        self.lastname = firstname
        self.email = email
        # self.my_id=my_id
        self.picture_url=picture_url
        self.username=username

    def __repr__(self):
        return '<ROW with label: User ID %r>' % self.id


class Poem(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255))
    body = db.Column(db.Text)
    user_id =db.Column(db.Integer)
    poem_type=db.Column(db.String(255))
    tags=db.Column(db.String(255))


    def __init__(self, title, body,user_id,poem_type,tags):
        self.title = title
        self.body = body
        self.user_id= user_id
        self.poem_type=poem_type
        self.tags=tags

    def __repr__(self):
        return '<ROW with label: User ID %r>' % self.id



if __name__ == '__main__':
    manager.run()