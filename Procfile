#release: python manage.py migrate
#web: gunicorn BypassDM.wsgi:application
#static: python manage.py collectstatic

web: python manage.py makemigrations && python manage.py migrate && python manage.py collectstatic && gunicorn AppNAME.wsgi

