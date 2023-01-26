from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import City, Course, Student

# Create your views here.
def reg_fun(request):
    return render(request, 'Registration.html', {'data':''})

def regdata_fun(request):
    user_name = request.POST['txtUserName']
    user_email = request.POST['txtEmail']
    user_pswd = request.POST['txtPswd']

    if User.objects.filter(Q(username=user_name) | Q(email=user_email)).exists():
        return render(request, 'Registration.html', {'data':'Username, email and password is already exist'})
    else:
        u1 = User.objects.create_superuser(username = user_name, email = user_email, password = user_pswd)
        u1.save()
        return redirect('log')

def log_fun(request):
    return render(request, 'Login.html', {'data':''})

def logdata_fun(request):
    user_name = request.POST['txtUserName']
    user_pswd = request.POST['txtPswd']
    user1 = authenticate(username = user_name, password = user_pswd) # It is camparing that data is exist or not
    if user1 is not None:
        if user1.is_superuser:
            login(request, user1)
            return redirect('home')
        else:
            return render(request, 'Login.html', {'data': 'User is not superuser'})
    else:
        return render(request, 'Login.html', {'data': 'Enter proper username and password'})


def home_fun(request):
    return render(request, 'home.html')


def addstudents_fun(request):
    city = City.objects.all()
    course = Course.objects.all()
    return render(request, 'addstudent.html', { 'City_Data': city, 'Course_Data': course })


def readdata_fun(request):
    s1 = Student()
    s1.Stud_Name = request.POST['txtName']
    s1.Stud_Age = request.POST['txtAge']
    s1.Stud_Phno = request.POST['txtPhno']
    s1.Stud_City = City.objects.get(City_Name = request.POST['ddlCity'])
    s1.Stud_Course = Course.objects.get(Course_Name = request.POST['ddlCourse'])
    s1.save()
    return redirect('add')


def display_fun(request):
    s1 = Student.objects.all()
    return render(request, 'display.html', {'data' : s1})


def update_fun(request, id):
    s1 = Student.objects.get(id = id)
    city = City.objects.all()
    course = Course.objects.all()

    if  request.method == 'POST':
        s1.Stud_Name = request.POST['txtName']
        s1.Stud_Age = request.POST['txtAge']
        s1.Stud_Phno = request.POST['txtPhno']
        s1.Stud_City = City.objects.get(City_Name=request.POST['ddlCity'])
        s1.Stud_Course = Course.objects.get(Course_Name=request.POST['ddlCourse'])
        s1.save()
        return redirect('display')
    return render(request, 'update.html', {'data': s1, 'City_Data': city, 'Course_Data': course})


def delete_fun(request, id):
    s1 = Student.objects.get(id = id)
    s1.delete()
    return redirect('display')


def log_out_fun(request):
    return redirect('log')
