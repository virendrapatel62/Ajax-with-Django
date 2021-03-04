from django.shortcuts import render 
from django.http import JsonResponse , QueryDict
from .models import EmployeeForm , OfficeForm , Office , Employee

from django.forms.models import model_to_dict
from django.core import serializers
import json
# Create your views here.
  

def home(request):
    officeForm = OfficeForm()
    employeeForm = EmployeeForm()
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
        office = employee.office
        print(office)
        officeJson = model_to_dict(office)
        
        response = model_to_dict(employee)
        response['office'] = officeJson
        
        return JsonResponse(response)

    if request.method == "PUT":
        data = QueryDict(request.body)
        print(json.load(request.body))
        res = {}
        return JsonResponse(res)
    

def getAllOffices(request):
    offices = Office.objects.all()
    data = serializers.serialize("json" , offices)
    return JsonResponse( data , safe=False)

def getAllEmployees(request):
    employees = Employee.objects.all()
    data = serializers.serialize("json" , employees , use_natural_foreign_keys=True)
    return JsonResponse( data , safe=False)


def showEmployeePage(request):
    
    employeeForm = EmployeeForm()
    context = {
        
        "employeeForm" : employeeForm
    }
    return render(request ,template_name="employee-page.html" , context = context)

def showOfficePage(request):
    officeForm = OfficeForm()
   
    context = {
        "officeForm" : officeForm 
        
    }
    return render(request ,template_name="office-page.html" , context=context)