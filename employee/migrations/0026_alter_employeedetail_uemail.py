# Generated by Django 5.0.1 on 2024-04-05 16:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0025_alter_employeedetail_uemail'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employeedetail',
            name='uemail',
            field=models.EmailField(max_length=254),
        ),
    ]