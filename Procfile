#web: python manage.py makemigrations && python manage.py migrate && gunicorn BypassDM.wsgi:application

web: gunicorn BypassDm.wsgi
release: python manage.py migrate
