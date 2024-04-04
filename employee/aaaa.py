from django.contrib.admin.views.decorators import staff_member_required
from django.shortcuts import render, redirect
from .models import *
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from .models import EmployeeDetail, EmployeeExperience, EmployeeSkills, UserSignup
from django.contrib.auth.hashers import make_password
from django.contrib import messages



# Create your views here.


def index(request):
    return render(request, 'index.html')


def registration(request):
    error = ""
    if request.method == "POST":
        fn = request.POST['firstname']
        ln = request.POST['lastname']
        ec = request.POST['empcode']
        em = request.POST['email']
        pwd = request.POST['pwd']
        try:
            user = User.objects.create_user(first_name=fn, last_name=ln, username=em, password=pwd)
            EmployeeDetail.objects.create(user=user, empcode=ec)
            EmployeeExperience.objects.create(user=user)
            EmployeeSkills.objects.create(user=user)
            error = "no"
        except:
            error = "yes"
    return render(request, 'registration.html', locals())


def emp_login(request):
    error = ""
    if request.method == "POST":
        u = request.POST['emailid']
        p = request.POST['password']
        user = authenticate(username=u, password=p)
        print(u)
        print(p)
        print(user)
        if user:
            login(request, user)
            error = "no"
        else:
            error = "yes"
    return render(request, 'emp_login.html', locals())


def emp_home(request):
    if not request.user.is_authenticated:
        return redirect('emp_login')
    return render(request, 'emp_home.html')


def emp_change_password(request):
    if not request.user.is_authenticated:
        return redirect('emp_login')
    error = ""
    user = request.user
    if request.method == "POST":
        c = request.POST['currentpassword']
        n = request.POST['newpassword']
        try:
            if user.check_password(c):
                user.set_password(n)
                user.save()
                error = "no"
            else:
                error = "not"
        except:
            error = "yes"
    return render(request, 'emp_change_password.html', locals())


def Logout(request):
    logout(request)
    return redirect('index')


def profile(request):
    if not request.user.is_authenticated:
        return redirect('emp_login')
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
            error = "no"
        except:
            error = "yes"
    return render(request, 'profile.html', locals())


def my_experience(request):
    if not request.user.is_authenticated:
        return redirect('emp_login')
    user = request.user
    experience = EmployeeExperience.objects.get(user=user)

    return render(request, 'my_experience.html', locals())


def edit_myexperience(request):
    if not request.user.is_authenticated:
        return redirect('emp_login')
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
            error = "no"
        except:
            error = "yes"
    return render(request, 'edit_myexperience.html', locals())


def my_skills(request):
    if not request.user.is_authenticated:
        return redirect('emp_login')
    user = request.user
    skills = EmployeeSkills.objects.get(user=user)

    return render(request, 'my_skills.html', locals())


def edit_myskills(request):
    if not request.user.is_authenticated:
        return redirect('emp_login')
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
            error = "no"
        except:
            error = "yes"
    return render(request, 'edit_myskills.html', locals())


def user_signup(request):
    if request.method == 'POST':
        firstname = request.POST.get('firstname')
        lastname = request.POST.get('lastname')
        email = request.POST.get('email')
        password = request.POST.get('password')

        # Create a new user
        user = UserSignup(firstname=firstname, lastname=lastname, username=email, password=password)
        user.save()

        return redirect('user_login')  # Redirect to login page after successful signup
    else:
        return render(request, 'user_signup.html')

def user_login(request):
    error = None  # Initialize error variable
    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')

        try:
            user = UserSignup.objects.get(email=email)
        except UserSignup.DoesNotExist:
            error = "yes"  # Set error to 'yes' if user does not exist
            return render(request, 'user_login.html', {'error': error})

        if user.password == password:
            login(request, user)
            request.session.set_expiry(1800)
            error = "no"
            return redirect('user_home')  # Redirect to user_home page upon successful login
        else:
            error = "yes"  # Set error to 'yes' if password does not match
            return render(request, 'user_login.html', {'error': error})
    else:
        return render(request, 'user_login.html')

def user_change_password(request):
    if not request.user.is_authenticated:
        return redirect('user_login')
    error = ""
    user = request.user_signup
    if request.method == "POST":
        c = request.POST['currentpassword']
        n = request.POST['newpassword']
        try:
            if user.check_password(c):
                user.set_password(n)
                user.save()
                error = "no"
            else:
                error = "not"
        except:
            error = "yes"
    return render(request, 'user_change_password.html', locals())


def user_profile(request):
    if not request.user.is_authenticated:
        return redirect('user_login')
    error = ""
    # Retrieve the UserSignup object associated with the user
    user_signup = request.user.user_signup
    if request.method == "POST":
        fn = request.POST['firstname']
        ln = request.POST['lastname']
        contact = request.POST['contact']
        ddate = request.POST['ddate']
        gender = request.POST['gender']
        useraddress = request.POST['useraddress']

        # Update the fields of UserSignup object
        user_signup.first_name = fn
        user_signup.last_name = ln
        user_signup.contact = contact
        user_signup.gender = gender
        user_signup.useraddress = useraddress

        if ddate:
            user_signup.dateofbirth = ddate

        try:
            user_signup.save()
            error = "no"
        except:
            error = "yes"
    return render(request, 'user_profile.html', locals())



def user_home(request):
    if not request.user.is_authenticated:
        return redirect('user_login')

    return redirect(request, 'user_home.html')

def admin_login(request):
    error = ""
    if request.method == "POST":
        u = request.POST.get('username')
        p = request.POST.get('pwd')
        user = authenticate(username=u, password=p)
        if user is not None and user.is_staff:
            login(request, user)
            error = "no"
        else:
            error = "yes"
    return render(request, 'admin_login.html', {'error': error})


def admin_home(request):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    return render(request, 'admin_home.html')


def admin_change_password(request):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    error = ""
    user = request.user
    if request.method == "POST":
        c = request.POST['currentpassword']
        n = request.POST['newpassword']
        try:
            if user.check_password(c):
                user.set_password(n)
                user.save()
                error = "no"
            else:
                error = "not"
        except:
            error = "yes"
    return render(request, 'admin_change_password.html', locals())


def all_employees(request):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    employee = EmployeeDetail.objects.all()
    return render(request, 'all_employees.html', locals())


def edit_profile(request):
    if not request.user.is_authenticated:
        return redirect('admin_login')
