from django.shortcuts import render,redirect

from django.http import HttpResponse,JsonResponse

from myApp.models import *
from myProject.forms import *


def myStudent(request):
    
    student=Student_Model.objects.all()
    
    form=Student_Form()
    
    if request.method=="POST":
        
        student_form=Student_Form(request.POST)
        
        if student_form.is_valid():
            
            student_form.save()
        
    return render(request,'student.html',{'form':form,'student':student})


def editStudent(request,myid):
    
    student=Student_Model.objects.get(id=myid)
    
    form=Student_Form(instance=student)
    
    if request.method=="POST":
        
        form=Student_Form(request.POST,instance=student)
        
        if form.is_valid():
            form.save()
            
    return render(request,'editStudent.html',{'form':form})
    
def deleteStudent(request,myid):
    
    student=Student_Model.objects.filter(id=myid)
    
    student.delete()
    
    return redirect("myStudent")

