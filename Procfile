release: python manage.py migrate
web: gunicorn BypassDM.wsgi:application
static: python manage.py collectstatic
