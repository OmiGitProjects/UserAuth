from django.db import models

class EmployeeDetail(models.Model):
    emp_name = models.CharField(max_length=50)
    department = models.TextField()
    email = models.EmailField()
    phone = models.IntegerField()

    def __str__(self):
        return f"{self.emp_name}"