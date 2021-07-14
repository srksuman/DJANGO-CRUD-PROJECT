from django.db import models
from django.core import validators
from django import forms
# Create your models here.
class Student(models.Model):
    def checknumber(value):
        if len(str(value)) !=10:
            raise forms.ValidationError("Entered incorrect mobile number")
        

    student_field = (
        ('BIT','BIT'),
        ('BBA','BBA'),
        ('MSCIT','MSCIT'),
        ('CSIT','CSIT')
    )
    full_name = models.CharField(max_length=70,help_text="Enter your full name",error_messages={'required':'You cannot leave name field empty'})
    address = models.CharField(max_length=70)
    phone_number = models.IntegerField(validators=[checknumber],help_text="Your number must contain 10 digits")
    field = models.CharField(max_length=70,choices=student_field,default='BIT')
    picture = models.ImageField(upload_to='images/')