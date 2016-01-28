from __future__ import absolute_import
from django.conf.urls import url, include
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    url(r'^', include('django_alexa.urls')),
] + staticfiles_urlpatterns()
