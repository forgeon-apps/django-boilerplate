[![Deploy with Forgeon](https://forgeon.io/images/button-deploy/png/deploy-to-forgeon-6.png)](https://forgeon.io/projects?import=1&no_upload=1&auto=0&git_url=https%3A%2F%2Fgithub.com%2Fforgeon-apps%2Fdjango-boilerplate)

# Django + Forgeon

This example shows how to use Django 4 on Forgeon with Serverless Functions using the [Python Runtime](https://forgeon.io/docs/concepts/functions/serverless-functions/runtimes/python).

## Demo

https://django-template.forgeon.io/

## How it Works

Our Django application, `example` is configured as an installed application in `api/settings.py`:

```python
# api/settings.py
INSTALLED_APPS = [
    # ...
    'example',
]
```

We allow "\*.forgeon.io" subdomains in `ALLOWED_HOSTS`, in addition to 127.0.0.1:

```python
# api/settings.py
ALLOWED_HOSTS = ['127.0.0.1', '.forgeon.io']
```

The `wsgi` module must use a public variable named `app` to expose the WSGI application:

```python
# api/wsgi.py
app = get_wsgi_application()
```

The corresponding `WSGI_APPLICATION` setting is configured to use the `app` variable from the `api.wsgi` module:

```python
# api/settings.py
WSGI_APPLICATION = 'api.wsgi.app'
```

There is a single view which renders the current time in `example/views.py`:

```python
# example/views.py
from datetime import datetime

from django.http import HttpResponse


def index(request):
    now = datetime.now()
    html = f'''
    <html>
        <body>
            <h1>Hello from Forgeon!</h1>
            <p>The current time is { now }.</p>
        </body>
    </html>
    '''
    return HttpResponse(html)
```

This view is exposed a URL through `example/urls.py`:

```python
# example/urls.py
from django.urls import path

from example.views import index


urlpatterns = [
    path('', index),
]
```

Finally, it's made accessible to the Django server inside `api/urls.py`:

```python
# api/urls.py
from django.urls import path, include

urlpatterns = [
    ...
    path('', include('example.urls')),
]
```

This example uses the Web Server Gateway Interface (WSGI) with Django to enable handling requests on Forgeon with Serverless Functions.

## Running Locally

```bash
python manage.py runserver
```

Your Django application is now available at `http://localhost:8000`.

## One-Click Deploy

Deploy the example using [Forgeon](https://forgeon.io?utm_source=github&utm_medium=readme&utm_campaign=forgeon-examples):

[![Deploy with Forgeon](https://forgeon.io/images/button-deploy/png/deploy-to-forgeon-6.png)](https://forgeon.io/projects?import=1&no_upload=1&auto=0&git_url=https%3A%2F%2Fgithub.com%2Fforgeon-apps%2Fdjango-boilerplate)