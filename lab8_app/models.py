from django.db import models

class Department(models.Model):
    department_name = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    room_number = models.IntegerField()

    def __str__(self):
        return self.department_name


class Position(models.Model):
    position_name = models.CharField(max_length=100)
    salary = models.DecimalField(max_digits=10, decimal_places=2)
    bonus_percentage = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return self.position_name


class Employee(models.Model):
    last_name = models.CharField(max_length=50)
    first_name = models.CharField(max_length=50)
    middle_name = models.CharField(max_length=50, blank=True)
    address = models.CharField(max_length=255, blank=True)
    phone = models.CharField(max_length=15)
    education = models.CharField(max_length=50)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    position = models.ForeignKey(Position, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Project(models.Model):
    project_name = models.CharField(max_length=100)
    deadline = models.DateField()
    funding = models.DecimalField(max_digits=15, decimal_places=2)

    def __str__(self):
        return self.project_name


class ProjectExecution(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    start_date = models.DateField()

    def __str__(self):
        return f"{self.project} - {self.department} - {self.start_date}"
