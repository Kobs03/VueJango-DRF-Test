# Generated by Django 5.0.4 on 2024-05-06 03:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('EmployeeApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('EmployeeId', models.AutoField(primary_key=True, serialize=False)),
                ('Department', models.CharField(max_length=500)),
                ('DateOfJoining', models.DateField()),
                ('EmployeeName', models.CharField(max_length=500)),
                ('PhotoFileName', models.CharField(max_length=500)),
            ],
        ),
        migrations.RenameField(
            model_name='department',
            old_name='EmployeeId',
            new_name='DepartmentId',
        ),
        migrations.RenameField(
            model_name='department',
            old_name='Department',
            new_name='DepartmentName',
        ),
        migrations.RemoveField(
            model_name='department',
            name='DateOfJoining',
        ),
        migrations.RemoveField(
            model_name='department',
            name='EmployeeName',
        ),
        migrations.RemoveField(
            model_name='department',
            name='PhotoFileName',
        ),
    ]
