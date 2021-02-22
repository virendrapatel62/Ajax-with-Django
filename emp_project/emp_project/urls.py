from django.contrib import admin
from django.urls import path
from emp_project.emp_app.views import home , officeCrud , employeeCrud , getAllOffices

urlpatterns = [
    path('admin/', admin.site.urls),
    path('' , home , name='home'), 
    path('office' , officeCrud), 
    path('employee' , employeeCrud), 
    path("offices" , getAllOffices)
]
