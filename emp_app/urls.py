from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="All Chats"),
    path('add_employee', views.addEmployee, name="Add Employee"),
    path('get_all_employees', views.getAllEmployees, name="Get All Employee")
   ]
