# Generated by Django 5.0.1 on 2024-04-05 16:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0023_delete_usersignup_employeedetail_dateofbirth_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employeedetail',
            name='uemail',
            field=models.EmailField(default='', max_length=100),
        ),
    ]
