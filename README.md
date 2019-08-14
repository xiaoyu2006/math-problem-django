# A web-application developed with Django
The settings of this web-application is for Heroku so it can't run on localhost with command
```
python manage.py runserver
```
I ran it on Heroku: https://math-problem.herokuapp.com/


:-)
If you really want to run it on localhost, delete the following code in math_problem/settings.py
```
DEBUG = False
import dj_database_url
DATABASES={
   'default': dj_database_url.config(default='postgres://localhost')
}
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
ALLOWED_HOSTS = ['*']
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
STATIC_ROOT = 'staticfiles'
STATICFILES_DIRS=(
    os.path.join(BASE_DIR, 'static'),
)
```
