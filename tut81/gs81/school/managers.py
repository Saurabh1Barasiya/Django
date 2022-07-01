from django.db import models

class CustomManager(models.Manager):
    def get_queryset(self):
        # return super().get_queryset().order_by('-id')
        return super().get_queryset().order_by('-id')
    def get_stu_id_range(self,r1,r2):
        return super().get_queryset().filter(id__range=(r1,r2))
