# Generated by Django 5.0.1 on 2024-03-30 10:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0015_usersignup_contact_usersignup_dateofbirth_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='UserSignup',
            new_name='CustomUser',
        ),
    ]
