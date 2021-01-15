from django.contrib import admin

from .models import Patient


@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'middle_name', 'phone', 'email', 'date_of_birth', 'gender', 'is_citizen', 'nationality', 'identity_number', 'address', 'address2', 'city', 'zip_code','province')


