echo 'Making migration script automatically and then applying the changes to the database. for more: "http://blog.miguelgrinberg.com/post/flask-migrate-alembic-database-migration-wrapper-for-flask"'
cd  "$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
source venv/bin/activate
python manage.py db migrate
python manage.py db upgrade
echo 'Done... Manually verify using pgSQL'
heroku pg:psql
\d
