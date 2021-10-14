from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin, UserManager


class User(AbstractBaseUser, PermissionsMixin):

    username = models.CharField(max_length=30, unique=True)
    name = models.CharField('Nome', max_length=100)
    email = models.EmailField('E-Mail', max_length=100, unique=True)
    cpf = models.CharField('CPF', blank=True, null=True, max_length=11, unique=True)
    phone = models.CharField('Telefone', max_length=50, null=True, blank=True)
    is_active = models.BooleanField('ativo', default=True)
    is_staff = models.BooleanField('staff', default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    class Meta:
        verbose_name = 'usuário'
        verbose_name_plural = 'usuários'

