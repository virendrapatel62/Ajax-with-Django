from django.db import models
from django.forms import ModelForm
from django.forms.models import model_to_dict


class Office(models.Model):
    name=models.CharField(max_length=20)
    location=models.CharField(max_length=20)

    def __str__(self):
        return self.name;
    
    def natural_key(self):
        print("natural keys--office")
        return model_to_dict(self)


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
    active = models.BooleanField(default=True)

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
