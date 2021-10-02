from django import forms
from django.contrib.auth import forms as auth_forms
from django.contrib.auth.forms import UsernameField

from django.utils.translation import ugettext_lazy as _

from identity.models import User


class RegisterForm(auth_forms.UserCreationForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['password1'].widget.attrs.update(
            {'class': 'form-control mb-0', 'placeholder': _('Password')}
        )
        self.fields['password2'].widget.attrs.update(
            {'class': 'form-control', 'placeholder': _('Password confirmation')}
        )
        self.fields['username'].label_suffix = ''
        self.fields['password1'].label_suffix = ''
        self.fields['password2'].label_suffix = ''

    class Meta:
        model = User
        fields = ("username",)
        field_classes = {'username': UsernameField}

        widgets = {
            'username': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': _('Username')
            }),

        }


class LoginForm(auth_forms.AuthenticationForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update(
            {'class': 'form-control', 'placeholder': _('Username')}
        )
        self.fields['password'].widget.attrs.update(
            {'class': 'form-control', 'placeholder': _('Password')}
        )
        self.fields['username'].label_suffix = ''
        self.fields['password'].label_suffix = ''
