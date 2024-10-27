# Використовуйте базовий образ Python
FROM python:3.11

# Встановіть робочу директорію
WORKDIR /code
WORKDIR /app

# Скопіюйте файли проекту
COPY . /code/
COPY table_lab7.py /app/table_lab7.py

# Встановіть залежності
RUN pip install --no-cache-dir -r requirements.txt

# Відкрийте порт 8000
EXPOSE 8000


CMD ["python", "manage.py", "runserver", "0.0.0.0:8000", "table_lab7.py"]

# Lab8_password – пароль