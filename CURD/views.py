from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .serializers import departmentSerializer, employeeSerializer
from .models import department, employee


class DeparmentListCreate (ListCreateAPIView):
    queryset = department.objects.all()
    serializer_class = departmentSerializer

class DepartmentRUD (RetrieveUpdateDestroyAPIView):
    queryset = department.objects.all()
    serializer_class = departmentSerializer

class EmployeeListCreate (ListCreateAPIView):
    queryset = employee.objects.all()
    serializer_class = employeeSerializer

class EmployeeRUD (RetrieveUpdateDestroyAPIView):
    queryset = employee.objects.all()
    serializer_class = employeeSerializer        
