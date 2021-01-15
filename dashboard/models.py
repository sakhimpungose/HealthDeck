from django.db import models
from django.urls import reverse

from django.utils.translation import gettext_lazy as _


GENDER_CHOICES = (('F', 'Female'), ('M', 'Male'))

PROVINCE_CHOICES = (
    ('EC', 'Eastern Cape'),
    ('FS', 'Free State'),
    ('GP', 'Gauteng'),
    ('KZN', 'KwaZulu-Natal'),
    ('LP', 'Limpopo'),
    ('MP', 'Mpumalanga'),
    ('NC', 'Northern Cape'),
    ('NW', 'North West'),
    ('WC', 'Western Cape'),
)



class Patient(models.Model):
    first_name = models.CharField(_('first name'), max_length=32)
    middle_name = models.CharField(_('middle name'), max_length=32, blank=True)
    last_name = models.CharField(_('last name'), max_length=32, blank=True)

    phone = models.CharField(_('phone number'), max_length=10, blank=True)    
    email = models.EmailField(_('email address'), blank=True)    

    date_of_birth = models.DateField(_('date of birth'), null=True, blank=True)

    gender = models.CharField(_('gender'), choices=GENDER_CHOICES, max_length=1, blank=True)

    is_citizen = models.BooleanField(
        _('citizen'),
        default=True,
        blank=True,
    )
    nationality = models.CharField(_('nationality'), max_length=64, blank=True)
    identity_number = models.CharField(_('id or passport'), max_length=13, blank=True)

    address = models.CharField(_('address 1'), max_length=255, blank=True)
    address2 = models.CharField(_('address 2'), max_length=255, blank=True)
    city = models.CharField(_('city'), max_length=255, blank=True)
    zip_code = models.CharField(_('zip'), max_length=10, blank=True)
    province = models.CharField(_('province'), choices=PROVINCE_CHOICES, max_length=3, blank=True)

    def get_absolute_url(self):
        return reverse('dashboard:patient-detail', args=[str(self.id)])

    def __str__(self):
        return self.first_name

