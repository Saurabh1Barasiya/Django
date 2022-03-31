from django.contrib import admin
from .models import Student
# Register your models here.

class StudentAdmin(admin.ModelAdmin):
    list_display = ('stu_name', 'stu_email', 'stu_age', 'stu_phone')
admin.site.register(Student, StudentAdmin)
