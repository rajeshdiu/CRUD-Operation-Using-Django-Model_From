from django.contrib import admin

from myApp.models import*


class Student_Display(admin.ModelAdmin):
    
    list_display=['Name','Department','City']


admin.site.register(Student_Model,Student_Display)