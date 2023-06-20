from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.forms import ModelForm

class UserAdminCreationForm(UserCreationForm):
    """
    A custom form for creating new users.
    """

    first_name = forms.CharField(widget=forms.TextInput)
    last_name = forms.CharField(widget=forms.TextInput)

    class Meta:
        model = get_user_model()
        fields = ['phone_number', 'first_name', 'last_name']


class LoginForm(ModelForm):
    """
    Create and change/mark a login form fields
    """
    class Meta:
        model = get_user_model()
        fields = ['phone_number', 'password']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.user = None
