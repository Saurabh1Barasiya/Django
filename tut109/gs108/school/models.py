from django.urls import reverse
from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    password = models.CharField(max_length=50)
    
    # def get_absolute_url(self):
    #     return reverse("thanks")
    
    def get_absolute_url(self):
        return reverse("detail", kwargs={"pk": self.pk})
