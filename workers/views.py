import json
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse

from . import models
import datetime


def default(o):
    if isinstance(o, (datetime.date, datetime.datetime)):
        return o.isoformat()


@csrf_exempt
def create_position(request):
    if request.method == 'GET':
        positions = models.Position.objects.all()
        data = []
        for position in positions:
            data.append({'name': position.name, 'department': position.department})
        json_data = json.dumps(data)
        return JsonResponse(json_data, safe=False)
    if request.method == 'POST':
        data = json.loads(request.body)
        new_position = models.Position.objects.create(**data)
        json_data = {'name': new_position.name, 'department': new_position.department}
        return JsonResponse(json_data, safe=False)


@csrf_exempt
def create_employee(request):
    if request.method == 'GET':
        employees = models.Employee.objects.all()
        data = []
        for employee in employees:
            data.append({'name': employee.name, 'birth_date': employee.birth_date,
                         'salary': employee.salary, 'position': employee.position.id})
        json_data = json.dumps(data, default=default)
        return JsonResponse(json_data, safe=False)
    if request.method == 'POST':
        data = json.loads(request.body)
        new_employee = models.Employee.objects.create(**data)
        json_data = {'name': new_employee.name, 'birth_date': new_employee.birth_date,
                     'salary': new_employee.salary, 'position': new_employee.position.id}
        return JsonResponse(json_data, safe=False)


# class PositionViewSet(viewsets.ModelViewSet):
#     queryset = Position.objects.all()
#     serializer_class = PositionSerializer
#
#
# class EmployeeViewSet(viewsets.ModelViewSet):
#     queryset = Employee.objects.all()
#     serializer_class = EmployeeSerializer


