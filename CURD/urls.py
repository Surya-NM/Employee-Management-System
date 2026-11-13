from django.urls import path
from .views import EmployeeListCreate, EmployeeRUD, DeparmentListCreate, DepartmentRUD

urlpatterns =[
    path('Departments/', DeparmentListCreate.as_view()),
    path('Departments/<int:pk>/', DepartmentRUD.as_view()),
    path('Employees/', EmployeeListCreate.as_view()),
    path('Employees/<int:pk>/', EmployeeRUD.as_view())

]