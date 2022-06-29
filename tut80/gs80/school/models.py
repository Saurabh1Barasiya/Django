from django.db import models

# Create your models here.

# here both table are created.
class Exam_center(models.Model):
    cname = models.CharField(max_length=50)
    ccity = models.CharField(max_length=50)
   

class Student(Exam_center):
    roll = models.IntegerField()    # here roll is added to Exam_center table.
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    