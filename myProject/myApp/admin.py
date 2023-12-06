from django.contrib import admin

from myApp.models import*


class Student_Display(admin.ModelAdmin):
    
    list_display=['Name','Department','City','profile_pic']


admin.site.register(Student_Model,Student_Display)


class Teacher_Display(admin.ModelAdmin):
    
    list_display=['Name','Department','City']


admin.site.register(Teacher_Model,Teacher_Display)


class Employee_Display(admin.ModelAdmin):
    
    list_display=['Name','Department','City']
    
admin.site.register(Employee_Model,Employee_Display)