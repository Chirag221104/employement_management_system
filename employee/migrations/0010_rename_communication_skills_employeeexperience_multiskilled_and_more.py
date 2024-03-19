# Generated by Django 5.0.1 on 2024-03-01 16:15

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0009_rename_multiskilled_employeeexperience_communication_skills_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RenameField(
            model_name='employeeexperience',
            old_name='communication_skills',
            new_name='multiskilled',
        ),
        migrations.RemoveField(
            model_name='employeeexperience',
            name='customer_handling_skills',
        ),
        migrations.RemoveField(
            model_name='employeeexperience',
            name='physical_skills',
        ),
        migrations.RemoveField(
            model_name='employeeexperience',
            name='technical_skills',
        ),
        migrations.RemoveField(
            model_name='employeeexperience',
            name='time_management_skills',
        ),
        migrations.AddField(
            model_name='employeeexperience',
            name='comment',
            field=models.CharField(max_length=300, null=True),
        ),
        migrations.AddField(
            model_name='employeeexperience',
            name='major',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='employeeexperience',
            name='specialization',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='employeeexperience',
            name='yearsofexp',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.CreateModel(
            name='EmployeeSkills',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('technical_skills', models.CharField(max_length=200, null=True)),
                ('physical_skills', models.CharField(max_length=200, null=True)),
                ('time_management_skills', models.CharField(max_length=200, null=True)),
                ('communication_skills', models.CharField(max_length=200, null=True)),
                ('customer_handling_skills', models.CharField(max_length=200, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.DeleteModel(
            name='EmployeeExperiences',
        ),
    ]