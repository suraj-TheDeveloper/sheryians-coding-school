from django.urls import path
from .views import *

urlpatterns = [
    path("list/", CourseList, name="courses"),
]