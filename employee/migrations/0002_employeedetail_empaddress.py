# Generated by Django 5.0.1 on 2024-02-10 13:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='employeedetail',
            name='empaddress',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
