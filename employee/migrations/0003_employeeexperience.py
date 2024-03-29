# Generated by Django 5.0.1 on 2024-02-10 14:39

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0002_employeedetail_empaddress'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='EmployeeExperience',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('multiskilled', models.CharField(max_length=200, null=True)),
                ('specialiation', models.CharField(max_length=100, null=True)),
                ('yearsofexp', models.CharField(max_length=50, null=True)),
                ('major', models.CharField(max_length=100, null=True)),
                ('comment', models.CharField(max_length=300, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
