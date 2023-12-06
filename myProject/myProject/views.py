from django.shortcuts import render,redirect

from django.http import HttpResponse,JsonResponse

from myApp.models import *
from myProject.forms import *


def myStudent(request):
    
    student=Student_Model.objects.all()
    
    form=Student_Form()
    
    if request.method=="POST":
        
        student_form=Student_Form(request.POST,request.FILES)
        
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

def editTeacher(request,myid):
    
    
    teacher=Teacher_Model.objects.get(id=myid)
    
    form=Teacher_Form(instance=teacher)
    
    if request.method == 'POST':
        
        form=Teacher_Form(request.POST,instance=teacher)
        
        if form.is_valid():
            form.save()
            
    return render(request,'editTeacher.html',{'form':form})
    
def deleteStudent(request,myid):
    
    student=Student_Model.objects.filter(id=myid)
    
    student.delete()
    
    return redirect("myStudent")


def myTeacher(request):
    
    teacher=Teacher_Model.objects.all()
    
    teacherForm=Teacher_Form()
    
    if request.method == 'POST':
        teacherForm=Teacher_Form(request.POST)
        
        if teacherForm.is_valid():
            
            teacherForm.save()
            
            return redirect("myTeacher")
        
    return render(request,'teacher.html',{'form':teacherForm,'teacher':teacher})


def deleteTeacher(request,myid):
    
    teacher=Teacher_Model.objects.filter(id=myid)
    
    teacher.delete()
    return redirect("myTeacher")


def myEmployee(request):
    
    employee=Employee_Model.objects.all()
    
    form=Employee_Form()
    
    if request.method == 'POST':
        
        form=Employee_Form(request.POST)
        
        if form.is_valid():
            
            form.save()
            
            return redirect("myEmployee")
    else:
        form=Employee_Form()
    
    return render(request,'employee.html',{'form':form,'employee':employee})

def deleteEmployee(request,myid):
    
    employee=Employee_Model.objects.filter(id=myid)
    employee.delete()
    return redirect("myEmployee")


def editEmployee(request,myid):
    
    employee=Employee_Model.objects.get(id=myid)
    
    form=Employee_Form(instance=employee)
    
    if request.method == 'POST':
        
        form=Employee_Form(request.POST,instance=employee)
        
        if form.is_valid():
            form.save()
            
            return redirect("myEmployee")

    return render(request,'editEmployee.html',{'form':form})