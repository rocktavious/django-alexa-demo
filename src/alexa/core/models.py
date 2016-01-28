from __future__ import absolute_import
from django.db import models
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token


class AlexaUser(models.Model):
    """Extends built in User model with additional fields"""
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    debug_toolbar = models.BooleanField(default=False)


# every time a user logs in if they don't have a token it gets generated
@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, **kwargs):
    Token.objects.get_or_create(user=instance)
    AlexaUser.objects.get_or_create(user=instance)
