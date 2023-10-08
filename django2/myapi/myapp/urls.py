from django.urls import path
from . import views

urlpatterns = [
    path('api/employees/', views.emp_list, name='emp-list'),
]