from __future__ import absolute_import
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from alexa.core.models import AlexaUser


class AlexaUserInline(admin.StackedInline):
    model = AlexaUser
    can_delete = False
    verbose_name_plural = 'Alexa User Options'


class UserAdmin(UserAdmin):
    inlines = (AlexaUserInline, )


admin.site.unregister(User)
admin.site.register(User, UserAdmin)

# Text to put at the end of each page's <title>.
admin.site.site_title = 'Rockman Alexa'
# Text to put in each page's <h1>.
admin.site.site_header = 'Admin'
# Text to put at the top of the admin index page.
admin.site.index_title = ''
