from django.shortcuts import render 
from django.http import JsonResponse
from .models import EmployeeForm , OfficeForm , Office , Employee

from django.forms.models import model_to_dict
from django.core import serializers

# Create your views here.
  

def home(request):
    officeForm = OfficeForm()
    employeeForm = EmployeeForm();
    context = {
        "officeForm" : officeForm , 
        "employeeForm" : employeeForm
    }
    return render(request , 'index.html',  context=context)



def officeCrud(request):
    if request.method == "POST": 
        print(request.POST)
        officeForm = OfficeForm(request.POST)
        office = officeForm.save()
        
        return JsonResponse(model_to_dict(office) , safe=False)


def employeeCrud(request):
    if request.method == "POST": 
        print(request.POST)
        employeeForm = EmployeeForm(request.POST)
        employee = employeeForm.save()
        
        return JsonResponse(model_to_dict(employee))
    

def getAllOffices(request):
    offices = Office.objects.all()
    data = serializers.serialize("json" , offices)
    return JsonResponse( data , safe=False)

def getAllEmployees(request):
    employees = Employee.objects.all()
    data = serializers.serialize("json" , employees)
    return JsonResponse( data , safe=False)