from django.shortcuts import render
from .models import Employee, Position, Department,Project, ProjectExecution

def home(request):
    employees = Employee.objects.all()
    positions = Position.objects.all()
    departments = Department.objects.all()
    projects = Project.objects.all()  
    project_executions = ProjectExecution.objects.all()
    

    context = {
        'title': 'Відділ кадрів',
        'student_name': 'Цибань Богдан Васильович',
        'group': 'ІПЗ-22010бск',
        'employees': employees,
        'positions': positions,
        'departments': departments,
        'projects': projects, 
        'project_executions': project_executions,
    }
    return render(request, 'home.html', context)
