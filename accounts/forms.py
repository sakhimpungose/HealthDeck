from django import forms

from django.contrib.auth.forms import UserCreationForm

from .models import User, Organisation

from .models import GENDER_CHOICES

from django.utils.translation import gettext_lazy as _


class CustomUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm.Meta):
        model = User

        fields = ('first_name', 'middle_name', 'last_name', 'username', 'email', 'password1', 'password2', 'date_of_birth', 'gender')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['gender'].widget=forms.RadioSelect(choices=GENDER_CHOICES)


class OrganisationCreationForm(forms.ModelForm):

    class Meta:
        model = Organisation
        fields = ('name', 'description')
        widgets = {
            'description': forms.Textarea(attrs={'rows': 3}),
        }