from http.client import HTTPResponse
from json import loads
from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from emp_app.models import Employee

# Create your views here.
def index(request):
    user = request.user
    headers = request.headers
    print(headers)

    return JsonResponse({"key": "user"})

@csrf_exempt #it bypass the security token. i.e you can access it from anywhere
def addEmployee(request):
    if request.method == "POST" :
            body = request.body
            data = loads(body) # parse into dictionary object 
            print(data["name"]) 
            employee = Employee(name = data["name"], designation = data["designation"] )
            employee.save()
            return JsonResponse(data)
    else:
            return JsonResponse({"error" : "Not found"})

def getAllEmployees(request):
    employees = Employee.objects.all().values()
    print(employees[0]["name"])
    data = []
    for emp in employees:
        data.append(emp)

    return JsonResponse({"data" : data})

def updateEmployee(request, emp_id):
        print(emp_id)
        if request.method == "PUT":
            
            body = loads(request.body)
            employee = Employee.objects.get(emp_id = emp_id)
        
            for k in body:
                if k == "name":
                    employee.name = body['name']
                elif k == "designation":
                    employee.designation = body["designation"]

        
            employee.save()
       
        return JsonResponse({"data" : "Success fully updated"})

def deleteEmployee(request, emp_id):
        if request.method == "DELETE" :
            employee = Employee.objects.get(emp_id = emp_id)
            employee.delete()
       
        return JsonResponse({"data" : "Successfully deleted"})
