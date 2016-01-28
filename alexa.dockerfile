FROM python:2.7

RUN pip install \
    dj-database-url==0.3.0 \
    Django==1.8.1 \
    django-admin-bootstrapped==2.5.6 \
    django-bootstrap3==6.2.2 \
    django-braces==1.8.0 \
    django-debug-toolbar==1.4.0 \
    django-extensions==1.5.5 \
    django-rest-swagger==0.3.4 \
    djangorestframework==3.1.3 \
    djangorestframework-expiring-authtoken==0.1.3 \
    factory_boy==2.5.2 \
    flake8==2.4.0 \
    gevent==1.0.2 \
    gunicorn==19.3.0 \
    httpretty==0.8.10 \
    psycopg2==2.6 \
    pycrypto==2.6.1 \
    pyOpenSSL==0.15.1 \
    pytest-capturelog==0.7 \
    pytest-cov==1.8.1 \
    pytest-django==2.8.0 \
    pytest-mock==0.5.0 \
    pytest==2.7.0 \
    pytz==2015.4 \
    pyul==0.4.5 \
    requests==2.5.1 \
    six==1.9.0 \
    slackclient==0.15 \
    whitenoise==2.0.2

RUN mkdir -p /src /out /data /media /static
WORKDIR /src

ENV DJANGO_SETTINGS_MODULE=alexa.core.settings \
    PYTHONPATH=/src

EXPOSE 8000
CMD [ "gunicorn", "--config", "alexa.core.gunicorn", "alexa.core.wsgi"]

COPY ./src/ /src

RUN django-admin migrate
RUN django-admin collectstatic --noinput


