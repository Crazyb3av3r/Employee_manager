from django.shortcuts import render
from django.contrib.auth import get_user_model

from .models import CustomUser
from .forms import UserAdminCreationForm
from django.views.generic import CreateView
from django.urls import reverse_lazy


User = get_user_model()


class UserCreateView(CreateView):
    """
    view for creating a new object, with a response render by a template
    """

    model = CustomUser
    template_name = 'register.html'
    form_class = UserAdminCreationForm
    permission_required = None
    success_url = reverse_lazy('login')

    def form_valid(self, form):

        response = super().form_valid(form)
        cd = form.cleaned_data
        self.object.set_password(cd['password1'])
        self.object.save()
        print(self.object)
        return response

