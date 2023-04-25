from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="All Chats"),
    path('add_employee', views.addEmployee, name="Add Employee")
   ]
