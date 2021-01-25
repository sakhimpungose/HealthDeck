from django import forms
from .models import Patient, ChiefComplaint, Appointment

PATIENT_FIELDS = [
    'first_name',
    'middle_name',
    'last_name',
    'phone',
    'email',
    'date_of_birth',
    'gender',
    'nationality',
    'identity_number',
    'address1',
    'address2',
    'city',
    'zip_code',
    'province',
]

class PatientCreationForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(PatientCreationForm, self).__init__(*args, **kwargs)
        self.label_suffix = ""

        # Text fields
        self.fields['first_name'].widget.attrs.update({'class': 'form-control'})
        self.fields['middle_name'].widget.attrs.update({'class': 'form-control'})
        self.fields['last_name'].widget.attrs.update({'class': 'form-control'})
        self.fields['phone'].widget.attrs.update({'class': 'form-control'})
        self.fields['email'].widget.attrs.update({'class': 'form-control'})
        self.fields['date_of_birth'].widget.attrs.update({'class': 'form-control'})
        self.fields['nationality'].widget.attrs.update({'class': 'form-control'})
        self.fields['identity_number'].widget.attrs.update({'class': 'form-control'})
        self.fields['address1'].widget.attrs.update({'class': 'form-control'})
        self.fields['address2'].widget.attrs.update({'class': 'form-control'})
        self.fields['city'].widget.attrs.update({'class': 'form-control'})
        self.fields['zip_code'].widget.attrs.update({'class': 'form-control'})

        # Select fields
        self.fields['gender'].widget.attrs.update({'class': 'form-select', 'rows' : 3})
        self.fields['province'].widget.attrs.update({'class': 'form-select', 'rows' : 3})

    class Meta:
        model = Patient
        fields = PATIENT_FIELDS

CHIEF_COMPLAINT_FIELDS = [
    'patient',
    'date_of_observation',
    'complaints',
    'general_condition',
    'current_medication',
    'allergies',
    'blood_pressure',
    'pulse',
    'temp',
    'weight',
    'height',
    'unirene_dipstick',
    'bmi',
    'hiv',
    'immediate_action_taken',
    'diagnosis',
]

class ChiefComplaintCreationForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(ChiefComplaintCreationForm, self).__init__(*args, **kwargs)
        self.label_suffix = ""

        # Select fields
        self.fields['patient'].widget.attrs.update({'class': 'form-select'})

        # Text fields
        self.fields['date_of_observation'].widget.attrs.update({'class': 'form-control'})
        self.fields['complaints'].widget.attrs.update({'class': 'form-control'})
        self.fields['general_condition'].widget.attrs.update({'class': 'form-control'})
        self.fields['current_medication'].widget.attrs.update({'class': 'form-control'})
        self.fields['blood_pressure'].widget.attrs.update({'class': 'form-control'})
        self.fields['pulse'].widget.attrs.update({'class': 'form-control'})
        self.fields['temp'].widget.attrs.update({'class': 'form-control'})
        self.fields['weight'].widget.attrs.update({'class': 'form-control'})
        self.fields['height'].widget.attrs.update({'class': 'form-control'})
        self.fields['unirene_dipstick'].widget.attrs.update({'class': 'form-control'})
        self.fields['bmi'].widget.attrs.update({'class': 'form-control'})
        self.fields['hiv'].widget.attrs.update({'class': 'form-control'})  

        # Textarea fields
        self.fields['complaints'].widget.attrs.update({'class': 'form-control', 'rows' : 3})
        self.fields['general_condition'].widget.attrs.update({'class': 'form-control', 'rows' : 3})
        self.fields['current_medication'].widget.attrs.update({'class': 'form-control', 'rows' : 3})
        self.fields['allergies'].widget.attrs.update({'class': 'form-control', 'rows' : 3})
        self.fields['immediate_action_taken'].widget.attrs.update({'class': 'form-control', 'rows' : 3})
        self.fields['diagnosis'].widget.attrs.update({'class': 'form-control', 'rows' : 3})


    class Meta:
        model = ChiefComplaint
        fields = CHIEF_COMPLAINT_FIELDS



APPOINTMENT_FIELDS = [
    'patient',
    'date_of_appointment',
    'status',
    'comment',
]

class AppointmentCreationForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(AppointmentCreationForm, self).__init__(*args, **kwargs)
        self.label_suffix = ""

        self.fields['patient'].widget.attrs.update({'class': 'form-select'})
        self.fields['date_of_appointment'].widget.attrs.update({'class': 'form-control'})
        self.fields['status'].widget.attrs.update({'class': 'form-select'})
        self.fields['comment'].widget.attrs.update({'class': 'form-control', 'rows' : 3})



    class Meta:
        model = Appointment
        fields = APPOINTMENT_FIELDS


class SearchForm(forms.Form):
    term = forms.CharField(max_length=255, widget=forms.TextInput(attrs={'class':'form-control'}))

    