from django.db import models

# Create your models here.
class Student(models.Model):
    stu_name = models.CharField(max_length=255)
    stu_email = models.EmailField(max_length=255)
    stu_age = models.IntegerField()
    stu_phone = models.CharField(max_length=10)

    def __str__(self):
        return self.stu_name