from django.contrib import admin
from .models import *
# Register your models here.
@admin.register(Std)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'roll', 'city', 'marks', 'pass_date']


@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'idnum', 'city', 'salary', 'join_date']