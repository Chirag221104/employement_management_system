# Generated by Django 5.0.1 on 2024-04-07 02:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0027_usersignup_remove_employeedetail_dateofbirth_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='employeedetail',
            name='email',
            field=models.EmailField(default='', max_length=254, unique=True),
        ),
        migrations.AddField(
            model_name='employeedetail',
            name='password',
            field=models.CharField(default='', max_length=128),
        ),
    ]
