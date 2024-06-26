from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from EmployeeApp.models import Department, Employee
from EmployeeApp.serializers import DepartmentSerializer, EmployeeSerializer

# Create your views here.

@csrf_exempt
def departmentApi(request,id=0):


    if request.method=='GET':
        departments = Department.objects.all()
        departments_serializer=DepartmentSerializer(departments,many=True)
        return JsonResponse(departments_serializer.data,safe=False)
    
    
    elif request.method=='POST':
        department_data=JSONParser().parse(request)
        departments_serializer=DepartmentSerializer(data=department_data)
        if departments_serializer.is_valid():
            departments_serializer.save()
            return JsonResponse("Added Successfully",safe=False)
        return JsonResponse("Failed to Add",safe=False)
    

    elif request.method=='PUT':
        department_data=JSONParser().parse(request)
        department=Department.objects.get(DepartmentId=department_data['DepartmentId'])
        departments_serializer=DepartmentSerializer(department,data=department_data)
        if departments_serializer.is_valid():
            departments_serializer.save()
            return JsonResponse("Updated Successfully",safe=False)
        return JsonResponse("Failed to Update")
    

    elif request.method=='DELETE':
        department=Department.objects.get(DepartmentId=id)
        department.delete()
        return JsonResponse("Deleted Successfully",safe=False)

    