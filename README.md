# Help my poem

This is a Python web app for poets to share and improve their work.

##Installation
Use the following unix commands to install:
*If you don't have **virualenv** installed, use this command to install it before continuing.

1. ``git clone git@github.com:morganwallace/poem_site.git``

2.  ``virtualenv venv && source venv/bin/activate``

## Run local server for development
1. ``python app.py``
2. preview at http://localhost:5000/



##Documentation

#### Backend
* Flask
* Heroku
* Postgres

#### Frontend
Bootsrap 3.0
Jinja2 (templating)


##### Installed Packages (requirements.txt)
Flask==0.9
Flask-KVSession==0.6.1
Flask-Login==0.2.11
Flask-Migrate==1.2.0
Flask-SQLAlchemy==1.0
Flask-Script==2.0.5
Jinja2==2.6
Mako==1.0.0
MarkupSafe==0.23
SQLAlchemy==0.7.8
Werkzeug==0.8.3
alembic==0.6.5
itsdangerous==0.24
psycopg2==2.4.5
simplekv==0.9.2
six==1.7.3
wsgiref==0.1.2