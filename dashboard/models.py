from django.db import models
from django.urls import reverse

from django.utils.translation import gettext_lazy as _

from accounts.models import GENDER_CHOICES

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

    nationality = models.CharField(_('nationality'), max_length=64, blank=True)
    identity_number = models.CharField(_('id or passport'), max_length=13, blank=True)

    address1 = models.CharField(_('address'), max_length=255, blank=True)
    address2 = models.CharField(_('address 2'), max_length=255, blank=True)
    city = models.CharField(_('city'), max_length=255, blank=True)
    zip_code = models.CharField(_('zip'), max_length=10, blank=True)
    province = models.CharField(_('province'), choices=PROVINCE_CHOICES, max_length=3, blank=True)

    def get_absolute_url(self):
        return reverse('dashboard:patient-detail', args=[str(self.id)])

    def __str__(self):
        if self.last_name:
            return '#%s %s %s' % (self.id, self.first_name, self.last_name)
        
        return '#%s %s' % (self.id, self.first_name)


class ChiefComplaint(models.Model):
    patient = models.ForeignKey('Patient', on_delete=models.CASCADE, related_name='complaint')
    date_of_observation = models.DateTimeField(_('date & time of observation'))
    complaints = models.TextField(_('complaints'))
    general_condition = models.TextField(_('general condition'), blank=True)
    current_medication = models.TextField(_('current medication'), blank=True)
    allergies = models.TextField(_('allergies'), blank=True)

    blood_pressure = models.CharField(_('blood pressure (mmHg)'), max_length=255, blank=True)
    pulse = models.CharField(_('pulse (b/min)'), max_length=255, blank=True)

    temp = models.CharField(_('temp (°C)'), max_length=255, blank=True)
    weight = models.FloatField(_('weight (KG)'), null=True, blank=True)
    height = models.FloatField(_('height (CM/M)'), null=True, blank=True)
    unirene_dipstick = models.CharField(_('unirene dipstick'), max_length=255, blank=True)

    bmi = models.CharField(_('BMI'), blank=True, max_length=8)
    hiv = models.CharField(_('HIV test'), blank=True, max_length=255)

    immediate_action_taken = models.TextField(_('immediate action taken'), blank=True)
    diagnosis = models.TextField(_('diagnosis'), blank=True)

    def get_absolute_url(self):
        return reverse('dashboard:chief-complaint-detail', args=[str(self.id)])

    def __str__(self):
        return '%s %s %s' % (self.patient, self.date_of_observation, self.complaints) 

