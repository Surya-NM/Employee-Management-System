from django.db import models

class department (models.Model):
    name = models.CharField(max_length=50, default='')
    description = models.TextField(max_length=150, default='')
    created_at =models.DateTimeField(auto_now_add=True)

class employee (models.Model):
    name = models.CharField(max_length=50, default='')
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=10)
    department = models.ForeignKey(department,on_delete=models.PROTECT, related_name= "employee")
    salary = models.DecimalField(max_digits=8, decimal_places=2)
    joining_date = models.DateField(auto_now_add=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)