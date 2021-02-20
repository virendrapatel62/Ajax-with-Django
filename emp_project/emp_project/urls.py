from django.contrib import admin
from django.urls import path
from emp_project.emp_app.views import * 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('' , home)
]
