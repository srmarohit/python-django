from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="All Chats"),
    path('add_employee', views.addEmployee, name="Add Employee"),
    path('get_all_employees', views.getAllEmployees, name="Get All Employee"),
    path('update_employee/<str:emp_id>', views.updateEmployee, name="Update Employee"),
    path('delete_employee/<str:emp_id>', views.deleteEmployee, name="Delete Employee")
   ]
