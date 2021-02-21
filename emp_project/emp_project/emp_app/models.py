from django.db import models
from django.forms import ModelForm



class Office(models.Model):
    name=models.CharField(max_length=20)
    location=models.CharField(max_length=20)

    def __str__(self):
        return self.name;


class Employee(models.Model):

    genders = [
        ("M" , "Male"), 
        ("F" , "Female")
    ]
    first_name=models.CharField(max_length=20)
    last_name=models.CharField(max_length=20)
    email = models.EmailField()
    gender = models.CharField(max_length=20 , choices = genders ) 
    office = models.ForeignKey(Office , on_delete=models.CASCADE)

    def __str__(self):
        return self.email;
    

class OfficeForm(ModelForm):
    class Meta:
        model = Office
        fields = "__all__"

    
class EmployeeForm(ModelForm):
    class Meta:
        model = Employee
        fields = "__all__"
