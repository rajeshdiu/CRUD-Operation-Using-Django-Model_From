from django import forms
from myApp.models import Student_Model

class Student_Form(forms.ModelForm):
    Name = forms.CharField(max_length=100)
    Department = forms.CharField(max_length=100)
    City = forms.CharField(max_length=100)

    class Meta:
        model = Student_Model
        fields = ['Name', 'Department', 'City']
        widgets = {
            'Name': forms.TextInput(attrs={'class': 'custom-class'}),
            'Department': forms.Select(choices=[('IT', 'Information Technology'), ('CS', 'Computer Science')]),
            'City': forms.TextInput(attrs={'placeholder': 'Enter city'}),
        }
        labels = {
            'Name': 'Full Name',
            'Department': 'Student Department',
            'City': 'Student City',
        }
