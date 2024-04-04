from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.conf import settings
from django.shortcuts import redirect
# Create your models here.
from django.contrib.auth.models import AbstractUser


class EmployeeDetail(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    empcode = models.CharField(max_length=50)
    empaddress = models.CharField(max_length=100, null=True)
    empdept = models.CharField(max_length=100, null=True)
    designation = models.CharField(max_length=100, null=True)
    contact = models.CharField(max_length=15, null=True)
    gender = models.CharField(max_length=50, null=True)
    joiningdate = models.DateField(null=True)

    def __str__(self):
        return self.user.username


class EmployeeExperience(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    multiskilled = models.CharField(max_length=200, null=True)
    specialization = models.CharField(max_length=100, null=True)
    yearsofexp = models.CharField(max_length=50, null=True)
    major = models.CharField(max_length=100, null=True)
    comment = models.CharField(max_length=300, null=True)

    def __str__(self):
        return self.user.username


class EmployeeSkills(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    technical_skills = models.CharField(max_length=200, null=True)
    physical_skills = models.CharField(max_length=200, null=True)
    time_management_skills = models.CharField(max_length=200, null=True)
    communication_skills = models.CharField(max_length=200, null=True)
    customer_handling_skills = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.user.username


class UserSignup(models.Model):
    firstname = models.CharField(max_length=30)
    lastname = models.CharField(max_length=150)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)
    contact = models.CharField(max_length=15, null=True)
    gender = models.CharField(max_length=50, null=True)
    dateofbirth = models.DateField(null=True)
    last_login = models.DateTimeField(verbose_name='last login', blank=True, null=True)

    def __str__(self):
        return self.email


