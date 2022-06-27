from django.db import models
import datetime
# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=70)
    roll = models.IntegerField(unique=True,null=True)
    city = models.CharField(max_length=70)
    marks = models.IntegerField()
    pass_date = models.DateField()
       

class Teacher(models.Model):
    tname = models.CharField(max_length=70,default='')
    troll = models.IntegerField(unique=True,null=True,default=1)
    tcity = models.CharField(max_length=70, default='')
    tmarks = models.IntegerField(default=1)
    d = datetime.date.today()
    tpass_date = models.DateField(default=d)
    