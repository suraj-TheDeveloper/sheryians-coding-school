from django.shortcuts import render, redirect, get_object_or_404
from .models import Courses, Enrollment, Payments
from authentication.models import Students
from django.db.models import Sum
from authentication.decorators import student_login_required
from django.contrib import messages
import random
import string

# Create your views here.
def CourseList(request):
    courses = Courses.objects.all()
    enroll_ids = set()
    if 'student_id' in request.session:
        student_id = request.session['student_id']
        if student_id:
            enroll_ids = set(Enrollment.objects.filter(student = student_id).values_list("course", flat=True))
    print("enroll_ids", enroll_ids)
    return render(request, "courses/course_list.html", {'courses': courses, "enrollids": enroll_ids})

@student_login_required
def payment_page(request, id):
    course = Courses.objects.get(id=id)
    student_id = request.session['student_id']
    already_exists = Enrollment.objects.filter(student = student_id, course = id).exists()
    if already_exists:
        messages.error(request, "You already enrolled")
        return redirect("courses")
    return render(request, "courses/payment_method.html", {"course": course})

@student_login_required
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

@student_login_required
def success(request, id):
    payment_data = Payments.objects.get(id=id)
    return render(request, "courses/success.html", {"payment": payment_data})

@student_login_required
def failure(request):
    return render(request, "courses/failed.html")

@student_login_required
def payment_history(request):
    student_id = request.session['student_id']
    if student_id:
        payment_details = Payments.objects.filter(student_id=get_object_or_404(Students, id=student_id)).prefetch_related('course').order_by("-created_at")
        total_amount = payment_details.aggregate(total=Sum("amount"))
        print("total_amount", total_amount)
    return render(request, "courses/payments_history.html", { "payments": payment_details,
        "total_paid": total_amount, })
