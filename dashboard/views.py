from django.shortcuts import render

from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from .models import Patient

PATIENT_FIELDS = [
    'first_name', 'middle_name', 'last_name', 'phone',
    'email', 'date_of_birth', 'gender', 'is_citizen',
    'nationality', 'identity_number', 'address', 'address2',
    'city', 'zip_code', 'province',
]

class PatientCreate(CreateView):
    model = Patient
    fields = PATIENT_FIELDS

class PatientUpdate(UpdateView):
    model = Patient
    fields = PATIENT_FIELDS

class PatientDelete(DeleteView):
    model = Patient
    success_url = reverse_lazy('dashboard:patients')

class PatientListView(generic.ListView):
    model = Patient

class PatientDetailView(generic.DetailView):
    model = Patient