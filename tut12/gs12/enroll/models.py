from django.db import models

# Create your models here.
class Student(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    age = models.IntegerField()

    # ye autometic add kar dega hamko value enter karne ki need nahi h.
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.first_name