# Generated by Django 5.1.2 on 2024-10-27 20:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lab8_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TestModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
    ]
