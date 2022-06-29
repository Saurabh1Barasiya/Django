from django.contrib import admin
from .models import Exam_center, Student
# Register your models here.

@admin.register(Exam_center)
class Exam_centerAdmin(admin.ModelAdmin):
    list_display = ['id','cname', 'ccity']

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['id','roll','name', 'age','cname', 'ccity']