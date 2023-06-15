from django.shortcuts import render
from django.contrib.auth import get_user_model

from .models import CustomUser
from .forms import UserAdminCreationForm
from django.views.generic import CreateView


User = get_user_model()


class UserCreateView(CreateView):
    """
    view for creating a new object, with a response render by a template
    """

    model = CustomUser
    template_name = 'register'
    form_class = UserAdminCreationForm
    success_url = ...
    permission_required = None

    def form_valid(self, form):

        response = super().form_valid(form)
        cd = form.cleaned_data
        self.object.set_password(cd['password1'])
        self.object.save()
        print(self.object)
        return response
