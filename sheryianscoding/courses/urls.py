from django.urls import path
from .views import *

urlpatterns = [
    path("list/", CourseList, name="courses"),
    path("enrollcourse/<int:id>", payment_page, name="enroll"),
    path("payments/<int:id>", PaymentMethod, name="payments"),
    path("success/<int:id>", success, name="success"),
    path("failure/", failure, name="failure")
]