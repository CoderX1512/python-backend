
from django.http import JsonResponse
from .models import Emp


def emp_list(request):
    employees = [
        { "id": "1" , "firstname": "John","lastname":"Doe" ,"address": "Address of emp 1"},
        { "id": "2" , "firstname": "Alex","lastname":"White" ,"address": "Address of emp 2"},
        {"id": "3", "firstname": "Jane", "lastname": "Smith", "address": "Address of emp 3"},
        {"id": "4", "firstname": "Alice", "lastname": "Watson", "address": "Address of emp 4"},
    ]
    return JsonResponse({"employees": employees})