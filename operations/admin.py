from django.contrib import admin

# Register your models here.
from .models import Student
@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['id','full_name','address','phone_number','field','picture']