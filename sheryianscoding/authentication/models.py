from django.db import models
from courses.models import Courses

# Create your models here.
class Students(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    phone = models.IntegerField()
    email = models.EmailField()
    dob = models.DateField(blank=True, null=True)
    bio = models.TextField(blank=True, default="")
    pincode = models.IntegerField(blank=True, default=0)
    city = models.CharField(blank=True, default="")
    state = models.CharField(blank=True, default="")
    country = models.CharField(blank=True, default="")
    course_id = models.ForeignKey(Courses, on_delete=models.CASCADE, default=0)

    class Meta:
        db_table = 'Students'