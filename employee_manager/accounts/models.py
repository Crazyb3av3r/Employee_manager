from django.contrib.auth.models import AbstractUser, BaseUserManager
from phonenumber_field.modelfields import PhoneNumberField
from phonenumber_field.phonenumber import PhoneNumber
from django.db import models

from django.utils.translation import gettext_lazy as _


class CustomUserManager(BaseUserManager):
    """Define a model manager for User model with no username field."""

    def _create_user(self, phone_numer, email, password=None, **extra_fields):
        """Create and save a User with the given email, phone and password."""
        if not email:
            raise ValueError("Email jest obowiazkowy do wypelnienia!")
        if not phone_numer:
            raise ValueError("Telefon jest obowiazkowy do wypelnienia!")
        email = self.normalize_email(email)
        phone = PhoneNumber.from_string(phone_number=phone_numer, region='PL').as_e164
        user = self.model(email=email, phone=phone, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, phone_number, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, phone_number, **extra_fields)

    def create_superuser(self, email, phone_number, password=None, **extra_fields):
        """Create and save a SuperUser"""
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(email, phone_number, password, **extra_fields)


class CustomUser(AbstractUser):

    username = None
    email = models.EmailField(_("email address"), blank=True)
    phone_number = PhoneNumberField(blank=False, null=False, unique=True)

    USERNAME_FIELD = 'phone_number'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()
