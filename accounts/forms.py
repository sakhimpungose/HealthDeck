from django import forms

from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth.forms import (
    AuthenticationForm, PasswordResetForm, SetPasswordForm
)


from .models import User

from .models import GENDER_CHOICES

from django.utils.translation import gettext_lazy as _


# Used for creating users 
class CustomUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm.Meta):
        model = User

        fields = ('first_name', 'middle_name', 'last_name', 'phone', 'username', 'email', 'password1', 'password2', 'date_of_birth', 'gender')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.label_suffix = ""
        self.fields['gender'].widget=forms.RadioSelect(choices=GENDER_CHOICES)


# Used for login
class CustomAuthenticationForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.label_suffix = ""
        self.fields['username'].widget.attrs.update({'class': 'form-control', 'placeholder':'Email address'})
        self.fields['password'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Password'})

# Used for requesting password reset link
class CustomPasswordResetForm(PasswordResetForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.label_suffix = ""
        self.fields['email'].widget.attrs.update({'class': 'form-control', 'placeholder':'Email address'})

class CustomSetPasswordForm(SetPasswordForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.label_suffix = ""
        self.fields['new_password1'].widget.attrs.update({'class': 'form-control'})
        self.fields['new_password2'].widget.attrs.update({'class': 'form-control'})
        
