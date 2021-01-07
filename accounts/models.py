from django.db import models
from django.contrib.auth.models import AbstractUser

from .validators import AlphanumericUsernameValidator

from django.utils.translation import gettext_lazy as _


GENDER_CHOICES = (('F', 'Female'), ('M', 'Male'))

class User(AbstractUser):

    username_validator = AlphanumericUsernameValidator()

    username = models.CharField(
        _('username'),
        max_length=24,
        unique=True,
        help_text=_('A username only contains letters and numbers (the first character must be a letter).'),
        validators=[username_validator],
        error_messages={
            'unique': _("A user with that username already exists."),
        },
    )
    email = models.EmailField(_('email address'), primary_key=True)
    middle_name = models.CharField(_('middle name'), max_length=64, blank=True)
    date_of_birth = models.DateField(_('date of birth'))

    gender = models.CharField(_('gender'), choices=GENDER_CHOICES, max_length=1)

    USERNAME_FIELD = 'email'

    REQUIRED_FIELDS = ['username', 'date_of_birth']

class Organisation(models.Model):
    name = models.CharField(
        _('organisation name'),
        max_length=64,
        unique=True,
        error_messages = {
            'unique': _("An organisation with that name already exists."),
        }
    )

    description = models.TextField(_('description'), max_length=512, blank=True)

    owner = models.ForeignKey('User', on_delete=models.CASCADE)

    def __str__(self):
        return self.name


