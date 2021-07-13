from django.db import models

# Create your models here.
class Student(models.Model):
    student_field = (
        ('BIT','BIT'),
        ('BBA','BBA'),
        ('MSCIT','MSCIT'),
        ('CSIT','CSIT')
    )
    full_name = models.CharField(max_length=70)
    address = models.CharField(max_length=70)
    phone_number = models.IntegerField()
    field = models.CharField(max_length=70,choices=student_field)
    picture = models.ImageField(upload_to='images/')