from django.shortcuts import render,redirect
from .models import *
from django.contrib.auth import login,logout,authenticate
# Create your views here.
from django.contrib.auth.models import User
from .models import EmployeeDetail, EmployeeExperience, EmployeeSkills

def index(request):
    return render(request,'index.html')

def registration(request):
    error = ""
    if request.method == "POST":
        fn = request.POST['firstname']
        ln = request.POST['lastname']
        ec = request.POST['empcode']
        em = request.POST['email']
        pwd = request.POST['pwd']
        try:
            user = User.objects.create_user(first_name=fn,last_name=ln,username=em,password=pwd)
            EmployeeDetail.objects.create(user = user,empcode=ec)
            EmployeeExperience.objects.create(user=user)
            EmployeeSkills.objects.create(user=user)
            EmployeeQualities.objects.create(user=user)
            error = "no"
        except:
            error = "yes"
    return render(request,'registration.html',locals())


def emp_login(request):
    error = ""
    if request.method == "POST":
        u = request.POST['emailid']
        p = request.POST['password']
        user = authenticate(username=u,password=p)
        if user:
            login(request,user)
            error = "no"
        else:
            error = "yes"
    return render(request,'emp_login.html',locals())

def emp_home(request):
    if not request.user.is_authenticated:
        return  redirect('emp_login')
    return render(request,'emp_home.html')

def Logout(request):
    logout(request)
    return redirect('index')

def profile(request):
    if not request.user.is_authenticated:
        return  redirect('emp_login')
    error = ""
    user = request.user
    employee = EmployeeDetail.objects.get(user=user)
    if request.method == "POST":
        fn = request.POST['firstname']
        ln = request.POST['lastname']
        ec = request.POST['empcode']
        dept = request.POST['department']
        designation = request.POST['designation']
        contact = request.POST['contact']
        jdate = request.POST['jdate']
        gender = request.POST['gender']
        empaddress = request.POST['empaddress']

        employee.user.first_name = fn
        employee.user.last_name = ln
        employee.empcode = ec
        employee.empdept = dept
        employee.designation = designation
        employee.contact = contact
        employee.gender = gender
        employee.empaddress = empaddress

        if jdate:
            employee.joiningdate = jdate

        try:
            employee.save()
            employee.user.save()
            error="no"
        except:
            error="yes"
    return render(request,'profile.html',locals())

def admin_login(request):
    return render(request,'admin_login.html')

def my_experience(request):
    if not request.user.is_authenticated:
        return  redirect('emp_login')
    user = request.user
    experience = EmployeeExperience.objects.get(user=user)

    return render(request,'my_experience.html',locals())

def edit_myexperience(request):
    if not request.user.is_authenticated:
        return  redirect('emp_login')
    error = ""
    user = request.user
    experience = EmployeeExperience.objects.get(user=user)
    if request.method == "POST":
        multiskilled = request.POST['multiskilled']
        specialization = request.POST['specialization']
        yearsofexp = request.POST['yearsofexp']
        major = request.POST['major']
        comment = request.POST['comment']

        experience.multiskilled = multiskilled
        experience.specialization = specialization
        experience.yearsofexp = yearsofexp
        experience.major = major
        experience.comment = comment

        try:
            experience.save()
            error="no"
        except:
            error="yes"
    return render(request,'edit_myexperience.html',locals())

def my_skills(request):
    if not request.user.is_authenticated:
        return  redirect('emp_login')
    user = request.user
    skills = EmployeeSkills.objects.get(user=user)

    return render(request,'my_skills.html',locals())

def edit_myskills(request):
    if not request.user.is_authenticated:
        return  redirect('emp_login')
    error = ""
    user = request.user
    skills = EmployeeSkills.objects.get(user=user)
    if request.method == "POST":
        technical_skills = request.POST['technical_skills']
        physical_skills = request.POST['physical_skills']
        time_management_skills = request.POST['time_management_skills']
        communication_skills = request.POST['communication_skills']
        customer_handling_skills = request.POST['customer_handling_skills']

        skills.technical_skills = technical_skills
        skills.physical_skills = physical_skills
        skills.time_management_skills = time_management_skills
        skills.communication_skills = communication_skills
        skills.customer_handling_skills = customer_handling_skills

        try:
            skills.save()
            skills.user.save()
            error="no"
        except:
            error="yes"
    return render(request,'edit_myskills.html',locals())
