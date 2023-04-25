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
            print(data) 
            employee = Employee(name="rajat", designation="senior analyst")
            employee.save()
            return JsonResponse(data)
    else:
            return JsonResponse({"error" : "Not found"})
