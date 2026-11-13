from rest_framework import serializers  
from .models import employee, department

class departmentSerializer (serializers.ModelSerializer):
    class Meta :
        model = department
        fields = "__all__"
    def __str__(self):
        return self.name

class employeeSerializer (serializers.ModelSerializer):
      department = departmentSerializer( read_only=True)

      class Meta:
        model = employee
        fields = '__all__'
      def __str__(self):
            return self.name            