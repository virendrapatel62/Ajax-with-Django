from django.db import models



class Office(models.Model):
    name=models.CharField(max_length=20)
    location=models.CharField(max_length=20)


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
    