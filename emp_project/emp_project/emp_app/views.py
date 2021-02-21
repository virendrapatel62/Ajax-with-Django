from django.shortcuts import render 
from django.http import JsonResponse
from .models import EmployeeForm , OfficeForm

from django.forms.models import model_to_dict

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