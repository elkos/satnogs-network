from rest_framework.authtoken.models import Token

from django.contrib.auth.models import AbstractUser
from django.core.validators import MaxLengthValidator
from django.db import models
from django.db.models.signals import post_save


def gen_token(sender, instance, created, **kwargs):
    token = Token.objects.get(user=instance)
    if not token:
        Token.objects.crete(user=instance)


class User(AbstractUser):
    """Model for SatNOGS users."""

    bio = models.TextField(default='', validators=[MaxLengthValidator(1000)])

    def __unicode__(self):
        return self.username

post_save.connect(gen_token, sender=User)
