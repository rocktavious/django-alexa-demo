from __future__ import absolute_import
from django.conf.urls import url, include
from django.http import HttpResponse
from django.contrib import admin, auth
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
import debug_toolbar
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.include_root_view = False

urlpatterns = [
    url(r'^ping$', lambda x: HttpResponse('pong'), name="ping"),
    url(r'^', include('django_alexa.urls')),
    url(r'^', include(router.urls), name="v1"),
    url(r'^', include('rest_framework_swagger.urls')),
    url(r'^auth/', include('rest_framework.urls')),
    url(r'^token/', 'rest_framework_expiring_authtoken.views.obtain_expiring_auth_token', name="token"),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^__debug__/', include(debug_toolbar.urls)),
] + staticfiles_urlpatterns()
