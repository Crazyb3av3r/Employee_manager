from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django import forms


class UserAdminCreationForm(UserCreationForm):
    """
    A custom form for creating new users.
    """

    required_css_class = ...
    first_name = forms.CharField(widget=forms.TextInput)
    last_name = forms.CharField(widget=forms.TextInput)

    class Meta:
        model = get_user_model()
        fields = ['email' or 'phone', 'first_name', 'last_name']
        widgets = {
            ...
        }