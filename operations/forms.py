from django import forms
from django.forms import fields, widgets
from . models import Student 
class StudentForm(forms.ModelForm):
    class  Meta:
        model = Student
        fields = ['full_name','address','phone_number','field','picture']
        widgets = {
            'full_name' :forms.TextInput(attrs={'placeholder':'Suman Raj Khanal','class':'form-control','required':True}),
            'phone_number':forms.NumberInput(attrs={'placeholder':'9803955983','class':'form-control'}),
            'address':forms.TextInput(attrs={'placeholder':'Thali,Kathmandu','class':'form-control'}),
            'field':forms.Select(attrs={'class':'form-control'}),
            
        }