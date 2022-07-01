from django.db import models
from .managers import CustomManager
# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    objects = models.Manager() # The default manager
    student = CustomManager() # The custom manager
    
class ProxyStudent(Student):
    class Meta:
        proxy = True
        ordering = ['name']