from flask import Flask
from flask import render_template
from flask import session, request, make_response, jsonify, flash, url_for, redirect
from flask.ext.sqlalchemy import SQLAlchemy
from functools import wraps

app = Flask(__name__)


# Loads configuration from `config.py`
app.config.from_object('config')

app.config['SQLALCHEMY_DATABASE_URI'] = "postgres://sllynvkpwzcmnr:5QO8q__RWGhpNEowuVYs-OEXBZ@ec2-54-225-101-64.compute-1.amazonaws.com:5432/dblnmi4smbffiv"

####### Database classes/schema
from manage import db, User, Poem


# login required decorator
def login_required(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if 'user_id' in request.cookies:
            return f(*args, **kwargs)
        else:
            flash('You need to login first.')
            return redirect(url_for('signup'))
    return wrap


@app.route('/logout')
@login_required
def logout():
    resp.set_cookie('user_id', '')
    resp.set_cookie('username', '')
    session.pop('logged_in', None)
    flash('You were logged out.')
    return redirect(url_for('home'))



########  Routing

@app.route('/')
def home():
    poems=db.session.query(Poem.title, Poem.body).all()
    # all_users = User.query.all()
    app.logger.debug(poems)
    # user_id = request.cookies.get('user_id')
    # flash('Your user id is: '+user_id)
    return render_template('welcome.html',poems=poems)


@app.route('/add')
@login_required
def add():
    # all_users = User.query.all()
    # app.logger.debug( all_users)
    # user_id = request.cookies.get('user_id')
    # flash('Your user id is: '+user_id)
    return render_template('add.html')


@app.route('/adduser' , methods=['POST'])
def add_user():
    user_info=request.form
    app.logger.debug(user_info)
    user = User(firstname=user_info['firstname'],
        lastname=user_info['lastname'],
        email=user_info['email'],
        username=user_info['username'])
    
    #query database for unique email
    test = User.query.filter_by(email=user_info['email']).first()
    app.logger.debug(test)
    if test is None:
        #add record for new user
        app.logger.debug('new user')
        db.session.add(user)
        db.session.commit()
        resp = make_response(jsonify(success=True))

        #eventually make the cookie a token
        resp.set_cookie({'user_id': user.id,'username':user_info['username'],'fname':user_info['firstname']})
    else: 
        app.logger.debug('existing user')
        resp = make_response(jsonify(success=False,existing_email=user_info['email']))
    return resp
    #if user is new add it

@app.route('/signin' , methods=['POST'])
def signin():
    test=User.query.filter_by(username=request.form['username'])
    if test is not None:
        resp = make_response(jsonify(success=True))
        resp.set_cookie('user_id', user.id)
    else: 
        app.logger.debug('no username')
        resp = make_response(jsonify(success=False))
    return resp


@app.route('/addpoem' , methods=['POST'])
def add_poem():
    app.logger.debug(request.form)
    user_id = request.cookies.get('user_id')
    # app.logger.debug(user_id)
    #args to init a poem: title, body,user_id,poem_type,tags
    #add to database
    poem= Poem(
        title=request.form['title'],
        body=request.form['body'],
        user_id=user_id,
        poem_type="test",
        tags="test; something")
    db.session.add(poem)
    db.session.commit()
    resp = make_response(jsonify(success=True,title=request.form['title']))
    return resp



@app.route('/poem/<title>')
def poem(title):
    poem=db.session.query(Poem.title, Poem.body).filter(Poem.title==title)
    body=poem.first()[1]
    # app.logger.debug('opening /poem/'+title+'\n'+poem.all())
    return render_template('poem.html',title=title, body=body)   


@app.route('/poet/<name>')
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

@app.errorhandler(404)
def not_found_error(error):
    return render_template('404.html'), 404




if __name__ == '__main__':
    app.run(debug=True)

