from django.shortcuts import render
from django.contrib.auth import get_user_model, login, logout

from .models import CustomUser
from .forms import UserAdminCreationForm, LoginForm
from django.views.generic import CreateView, FormView
from django.urls import reverse_lazy
from django.shortcuts import redirect, render


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


class LoginView(FormView):

    template_name = "login.html"
    # success_url = reverse_lazy('home')
    form_class = LoginForm

    def form_valid(self, form):
        """If the form is valid and user was authenticated, redirect to the home page"""
        user = form.user
        login(self.request, user)
        return super().form_valid(form)

    def form_invalid(self, form):
        """If the form is invalid, redirect to the Registration URL"""
        return redirect('register')
