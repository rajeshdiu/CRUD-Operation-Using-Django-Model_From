from django import forms
from myApp.models import *

class Student_Form(forms.ModelForm):
    class Meta:
        model = Student_Model
        fields = ['Name', 'Department', 'City', 'profile_pic']
        labels = {
            'Name': 'Full Name',
            'Department': 'Student Department',
            'City': 'Student City',
            'profile_pic': 'Profile Picture',
        }
        widgets = {
            'Name': forms.TextInput(attrs={'class': 'custom-class'}),
            'Department': forms.Select(choices=[('IT', 'Information Technology'), ('CS', 'Computer Science')]),
            'City': forms.TextInput(attrs={'placeholder': 'Enter city'}),
        }
class Teacher_Form(forms.ModelForm):
    
    class Meta:
        model=Teacher_Model
        fields = ['Name', 'Department', 'City']
        labels = {
            'Name': 'Full Name',
            'Department': 'Teacher Department',
            'City': 'Teacher City',
        }
        
class Employee_Form(forms.ModelForm):
    
    Name = forms.CharField(max_length=100)
    Department = forms.CharField(max_length=100)
    City = forms.CharField(max_length=100)
    
    class Meta:
        model=Employee_Model
        fields=['Name','Department','City']
        labels={
            'Name':'Full Name',
            'Department': 'Employee Department',
            'City':'Employee City'
        }
        
    