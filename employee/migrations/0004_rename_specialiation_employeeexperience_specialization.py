# Generated by Django 5.0.1 on 2024-02-16 04:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0003_employeeexperience'),
    ]

    operations = [
        migrations.RenameField(
            model_name='employeeexperience',
            old_name='specialiation',
            new_name='specialization',
        ),
    ]
