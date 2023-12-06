from django.db import models

class Student_Model(models.Model):
    Name = models.CharField(max_length=100)
    Department = models.CharField(max_length=100)
    City = models.CharField(max_length=100)
    profile_pic = models.ImageField(upload_to="media/profile_pic", null=True)

    def __str__(self):
        return self.Name
    
class Teacher_Model(models.Model):
    
    Name=models.CharField(max_length=100)
    Department=models.CharField(max_length=100)
    City=models.CharField(max_length=100)
    
    
    def __str__(self):
        return self.Name
    
class Employee_Model(models.Model):
    
    Name=models.CharField(max_length=100)
    Department=models.CharField(max_length=100)
    City=models.CharField(max_length=100)
    
    
    def __str__(self):
        return self.Name
    
    