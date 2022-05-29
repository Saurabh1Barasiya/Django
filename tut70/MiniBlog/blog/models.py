from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=200)
    desc = models.TextField() # isme max_length dene ki need nahi h.
    