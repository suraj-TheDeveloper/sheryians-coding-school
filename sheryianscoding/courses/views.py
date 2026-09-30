from django.shortcuts import render, redirect, get_object_or_404
from .models import Courses, Enrollment, Payments
from authentication.models import Students
from django.contrib import messages
import random
import string

# Create your views here.
def CourseList(request):
    courses = Courses.objects.all()
    return render(request, "courses/course_list.html", {'courses': courses})

def payment_page(request, id):
    course = Courses.objects.get(id=id)
    student_id = request.session['student_id']
    already_exists = Enrollment.objects.filter(student = student_id, course = id).exists()
    if already_exists:
        messages.error(request, "You already enrolled")
        return redirect("courses")
    return render(request, "courses/payment_method.html", {"course": course})

def PaymentMethod(request, id):
    course = Courses.objects.get(id=id)
    student_id = request.session['student_id']
    if request.method == 'POST':
        object, create = Enrollment.objects.get_or_create(
            course = get_object_or_404(Courses, id=id), 
            student = get_object_or_404(Students, id=student_id)
        )
        card_holder_name = request.POST['card_holder_name']
        card_last4 = request.POST['card_number']
        print("card_last4", card_last4)
        payment = Payments.objects.create(
            card_holder_name=card_holder_name, 
            card_last4=card_last4, 
            enrollid=get_object_or_404(Enrollment, id=object.id), 
            status="success", 
            amount=course.price, 
            student=get_object_or_404(Students, id=student_id), 
            course=get_object_or_404(Courses, id=id), 
            card_type="visa", 
            transactionid=''.join(random.choices(string.ascii_uppercase + string.digits, k=6))
        )
        payment.save()
        success = True
        if success == True:
            return redirect('success', id=payment.id)
        else:
            return redirect('failure')

def success(request, id):
    payment_data = Payments.objects.get(id=id)
    return render(request, "courses/success.html", {"payment": payment_data})

def failure(request):
    return render(request, "courses/failed.html")