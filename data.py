import os
import django
from datetime import datetime

# Налаштування Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "django_lab8.settings")
django.setup()

from lab8_app.models import Department, Position, Employee, Project, ProjectExecution

def add_data():
    # Додавання даних у таблицю Department
    departments = [
        {'department_name': 'Програмування', 'phone': '+380501234567', 'room_number': 701},
        {'department_name': 'Дизайн', 'phone': '+380501234568', 'room_number': 702},
        {'department_name': 'Інформаційні технології', 'phone': '+380501234569', 'room_number': 703},
    ]
    
    for dep in departments:
        Department.objects.create(
            department_name=dep['department_name'],
            phone=dep['phone'],
            room_number=dep['room_number']
        )

    # Додавання даних у таблицю Position
    positions = [
        {'position_name': 'Інженер', 'salary': 3000.00, 'bonus_percentage': 17.00},
        {'position_name': 'Редактор', 'salary': 2000.00, 'bonus_percentage': 12.00},
        {'position_name': 'Програміст', 'salary': 3500.00, 'bonus_percentage': 13.00},
    ]
    
    for pos in positions:
        Position.objects.create(
            position_name=pos['position_name'],
            salary=pos['salary'],
            bonus_percentage=pos['bonus_percentage']
        )

    # Додавання даних у таблицю Employee
    employees = [
        ('Шевченко', 'Дмитро', 'Степанович', 'Львів, вул. Сихівська, 9', '+380501234579', 'середня', 2, 1),
        ('Бойко', 'Олег', 'Анатолійович', 'Київ, вул. Петра Могили, 16', '+380501234581', 'середня', 2, 3),
        ('Костенко', 'Анастасія', 'Вікторівна', 'Полтава, вул. Дружби, 19', '+380501234584', 'вища', 3, 2),
        ('Федоренко', 'Ярослав', 'Романович', 'Київ, вул. Костянтинівська, 21', '+380501234585', 'середня', 2, 2),
        ('Ковалев', 'Дарина', 'Ігорівна', 'Дніпро, вул. Грушевського, 23', '+380501234586', 'вища', 1, 3),
        ('Кудряшов', 'Олексій', 'Сергійович', 'Львів, вул. Винниченка, 27', '+380501234587', 'спеціальна', 3, 2),
        ('Тимошенко', 'Олена', 'Петрівна', 'Одеса, вул. Мечникова, 4', '+380501234588', 'вища', 1, 3),
        ('Степаненко', 'Ірина', 'Анатоліївна', 'Харків, вул. Сумська, 30', '+380501234589', 'вища', 2, 1),
        ('Кравченко', 'Марина', 'Олександрівна', 'Київ, вул. Січових Стрільців, 17', '+380501234590', 'вища', 2, 2),
        ('Соломко', 'Андрій', 'Валерійович', 'Львів, вул. Івана Франка, 22', '+380501234592', 'вища', 1, 3),
        ('Даниленко', 'Олена', 'Володимирівна', 'Запоріжжя, вул. Червоноармійська, 15', '+380501234593', 'спеціальна', 3, 1),
        ('Назаренко', 'Ярослав', 'Сергійович', 'Харків, вул. Пушкінська, 31', '+380501234594', 'середня', 3, 3),
        ('Левицька', 'Оксана', 'Ігорівна', 'Полтава, вул. Бажана, 9', '+380501234595', 'вища', 2, 2),
        ('Степанов', 'Софія', 'Андріївна', 'Запоріжжя, вул. Набережна, 14', '+380501234605', 'середня', 3, 1),
        ('Петренко', 'Петро', 'Петрович', 'Львів, вул. Шевченка, 5', '+380501234571', 'спеціальна', 2, 3),
        ('Сидоренко', 'Олег', 'Олегович', 'Одеса, вул. Леніна, 15', '+380501234572', 'середня', 1, 2),
        ('Гриценко', 'Анна', 'Сергіївна', 'Харків, вул. Гагаріна, 12', '+380501234573', 'вища', 2, 1),
    ]
    
    for emp in employees:
        Employee.objects.create(
            last_name=emp[0],
            first_name=emp[1],
            middle_name=emp[2],
            address=emp[3],
            phone=emp[4],
            education=emp[5],
            department=Department.objects.get(id=emp[6]),
            position=Position.objects.get(id=emp[7])
        )

    # Додавання проектів у таблицю Project
    projects = [
        ('Проект 001', '2024-12-31', 10000.00),
        ('Проект 002', '2025-01-15', 15000.00),
        ('Проект 003', '2025-02-20', 12000.00),
        ('Проект 004', '2025-03-30', 20000.00),
        ('Проект 005', '2025-04-10', 11000.00),
        ('Проект 006', '2025-05-05', 13000.00),
        ('Проект 007', '2025-06-12', 16000.00),
        ('Проект 008', '2025-07-15', 18000.00),
        ('Проект 009', '2025-08-20', 19000.00),
        ('Проект 010', '2025-09-30', 21000.00),
        ('Проект 011', '2025-10-05', 22000.00),
        ('Проект 012', '2025-11-15', 25000.00),
    ]
    
    for proj in projects:
        Project.objects.create(
            project_name=proj[0],
            deadline=datetime.strptime(proj[1], '%Y-%m-%d'),
            funding=proj[2]
        )

    # Додавання виконання проектів у таблицю ProjectExecution
    project_executions = [
        (1, 1, '2024-10-01'),  # Проект 001, відділ Програмування
        (2, 1, '2024-10-01'),  # Проект 002, відділ Програмування
        (5, 1, '2024-10-01'),  # Проект 003, відділ Програмування
        (6, 1, '2024-10-01'),  # Проект 004, відділ Програмування
        (7, 1, '2024-10-01'),  # Проект 005, відділ Програмування
        (3, 2, '2024-10-01'),  # Проект 006, відділ Дизайн
        (4, 2, '2024-10-01'),  # Проект 007, відділ Дизайн
        (8, 2, '2024-10-01'),  # Проект 008, відділ Дизайн
        (9, 2, '2024-10-01'),  # Проект 009, відділ Дизайн
        (10, 3, '2024-10-01'), # Проект 010, відділ Інформаційні технології
        (11, 3, '2024-10-01'), # Проект 011, відділ Інформаційні технології
        (12, 3, '2024-10-01'), # Проект 012, відділ Інформаційні технології
    ]
    
    for proj_exec in project_executions:
        ProjectExecution.objects.create(
            project=Project.objects.get(id=proj_exec[0]),
            department=Department.objects.get(id=proj_exec[1]),
            start_date=datetime.strptime(proj_exec[2], '%Y-%m-%d')
        )

if __name__ == "__main__":
    add_data()
    print("Дані успішно додано до бази даних.")
