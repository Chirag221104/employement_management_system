# Generated by Django 5.0.1 on 2024-03-30 11:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0016_rename_usersignup_customuser'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='CustomUser',
            new_name='UserSignup',
        ),
    ]