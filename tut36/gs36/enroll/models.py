from django.db import models
from django.core.validators import MinLengthValidator,MaxLengthValidator
# Create your models here.
class User(models.Model):
    name = models.CharField(validators=[MinLengthValidator(5)], max_length=20)
    email = models.EmailField(validators=[MinLengthValidator(5)], max_length=20)
    password = models.CharField(validators=[MinLengthValidator(5)], max_length=20)
