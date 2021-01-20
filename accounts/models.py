from django.db import models
from django.contrib.auth.models import AbstractUser

from django.utils.translation import gettext_lazy as _

from .validators import AlphanumericUsernameValidator


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
    phone = models.CharField(_('phone number'), max_length=10, blank=True)
    middle_name = models.CharField(_('middle name'), max_length=64, blank=True)
    date_of_birth = models.DateField(_('date of birth'))
    gender = models.CharField(_('gender'), choices=GENDER_CHOICES, max_length=1)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'date_of_birth', 'gender']
