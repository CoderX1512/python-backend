from django.shortcuts import render
from django.http import JsonResponse
from .models import Item


def item_list(request):
    items = [
        {"name": "Item 1", "description": "Description of Item 1"},
        {"name": "Item 2", "description": "Description of Item 1"},
    ]
    return JsonResponse({"items": items})