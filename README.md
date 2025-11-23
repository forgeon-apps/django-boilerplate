[![Deploy with Forgeon](https://forgeon.io/button)](https://forgeon.io/new/clone?repository-url=https%3A%2F%2Fgithub.com%2Fforgeon%2Fexamples%2Ftree%2Fmain%2Fpython%2Fdjango&demo-title=Django%20%2B%20Forgeon&demo-description=Use%20Django%204%20on%20Forgeon%20with%20Serverless%20Functions%20using%20the%20Python%20Runtime.&demo-url=https%3A%2F%2Fdjango-template.forgeon.io%2F&demo-image=https://assets.forgeon.io/image/upload/v1669994241/random/django.png)

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

[![Deploy with Forgeon](https://forgeon.io/button)](https://forgeon.io/new/clone?repository-url=https%3A%2F%2Fgithub.com%2Fforgeon%2Fexamples%2Ftree%2Fmain%2Fpython%2Fdjango&demo-title=Django%20%2B%20Forgeon&demo-description=Use%20Django%204%20on%20Forgeon%20with%20Serverless%20Functions%20using%20the%20Python%20Runtime.&demo-url=https%3A%2F%2Fdjango-template.forgeon.io%2F&demo-image=https%3A%2F%2Fdrive.google.com%2Fthumbnail%3Fid%3D1q6iiJ6482PK2VENhHpvtVYE2-I6L9zrA%26sz%3Dw1200)
