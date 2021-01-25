from django.contrib import admin

from .models import Patient, ChiefComplaint


@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'middle_name', 'phone', 'email', 'date_of_birth', 'gender', 'nationality', 'identity_number', 'address1', 'address2', 'city', 'zip_code','province')


@admin.register(ChiefComplaint)
class ChiefComplaintAdmin(admin.ModelAdmin):
    pass
