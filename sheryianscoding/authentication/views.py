from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import *
from .models import *
from .decorators import student_login_required

def Login(request):
    if request.method == 'POST':
        phone = request.POST['phone']
        student = Students.objects.filter(phone=phone).first()
        if student is not None:
            request.session['student_id'] = student.id
            return redirect("index")
        else:
            messages.error(request, 'invalid phone no')
            return redirect("login")
    else:
        logins = LoginForm()
    return render(request, "auth/login.html", {'form': logins})


def Logout(request):
    request.session.flush()
    return redirect("login")


def Register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        phone = request.POST['phone']
        register = RegisterForm(request.POST)
        if register.is_valid():
            Students.objects.create(first_name=first_name, last_name=last_name, email=email, phone=phone)
            return redirect("login")
        else:
            messages.error(request, "Invalid form details")
    else:
        register = RegisterForm()
    return render(request, "auth/register.html", {'form': register})

@student_login_required
def Profile(request):
    student_id = request.session.get('student_id')
    student = Students.objects.filter(id=student_id).first()
    return render(request, "auth/profile.html", {'student': student})