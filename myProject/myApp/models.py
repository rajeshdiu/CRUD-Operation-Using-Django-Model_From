from django.db import models

class Student_Model(models.Model):
    
    Name=models.CharField(max_length=100)
    Department=models.CharField(max_length=100)
    City=models.CharField(max_length=100)
    
    
    def __str__(self):
        return self.Name