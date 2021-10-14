from django.db import models
from accounts.models import User

class Cat(models.Model):

    user = models.ForeignKey(User, on_delete=models.PROTECT)
    name = models.CharField('Nome', max_length=100)
    color = models.CharField('Cor', max_length=50)
    birthdate = models.DateField('Aniversário')
