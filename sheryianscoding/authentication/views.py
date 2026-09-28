from django.shortcuts import render, redirect, get_object_or_404
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
            payload = {
                "student_id": student.id,
                "first_name": student.first_name,
                "last_name": student.last_name,
                "email": student.email 
            }
            response = redirect("index")
            response.set_cookie('student_details', payload, max_age=24*60*60)
            return response
        else:
            messages.error(request, 'invalid phone no')
            return redirect("login")
    else:
        logins = LoginForm()
    return render(request, "auth/login.html", {'form': logins})


def Logout(request):
    request.session.flush()
    response = redirect("index")
    response.delete_cookie('student_details')
    return response

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
    if not student_id:
        return render("login")
    student_profile = get_object_or_404(Students, id=student_id)
    if request.method == 'POST':
        form = ProfileForm(request.POST, instance=student_profile)
        if form.is_valid():
            form.save()
            messages.success(request, "your profile has been updated")
            return redirect("profile")
    else:
        form = ProfileForm(instance=student_profile)
    print("form", form)
    return render(request, "auth/profile.html", {
        'student': student_profile,
        'form': form,
        'courses': student_profile.course_id.all()
    })