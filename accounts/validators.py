import re

from django.core import validators
from django.utils.deconstruct import deconstructible
from django.utils.translation import gettext_lazy as _

@deconstructible
class AlphanumericUsernameValidator(validators.RegexValidator):
    regex = r'^[a-zA-Z][a-zA-Z0-9]+\Z'

    message = _(
        'Enter a valid username. This value may contain only letters, '
        'and numbers but the first character must be a letter.'
    )

    flags = 0


