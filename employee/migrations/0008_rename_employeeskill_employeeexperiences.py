# Generated by Django 5.0.1 on 2024-03-01 15:51

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0007_rename_employeeskills_employeeskill'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RenameModel(
            old_name='EmployeeSkill',
            new_name='EmployeeExperiences',
        ),
    ]
