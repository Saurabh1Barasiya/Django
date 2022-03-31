from django.db import models

# Create your models here.
class Student(models.Model):
    stu_id = models.IntegerField(primary_key=True)
    stu_name = models.CharField(max_length=20)
    stu_age = models.IntegerField() 
    stu_email = models.EmailField(default=True)
    stu_address = models.CharField(max_length=50)
    stu_pass = models.CharField(max_length=20)

    # if hamko baad me or bhi columns addd karne h to ham defult ka use karage.

    stu_comment = models.CharField(max_length=50,default=True)