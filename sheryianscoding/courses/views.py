from django.shortcuts import render
from .models import Courses

# Create your views here.
def CourseList(request):
    courses = Courses.objects.all()
    return render(request, "courses/course_list.html", {'courses': courses})