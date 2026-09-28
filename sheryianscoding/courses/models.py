from django.db import models
from authentication.models import Students

# Create your models here.
class Courses(models.Model):
    title = models.CharField(max_length=500)
    duration = models.CharField(max_length=100)
    price = models.IntegerField()
    description = models.TextField(max_length = 2000)
    thumbnail = models.ImageField(upload_to='courses/', null=True, blank=True)
    start_Date = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        db_table = "Courses"

class CourseModules(models.Model):
    courseid = models.ForeignKey(Courses, on_delete=models.CASCADE)
    module_name = models.CharField(max_length=100)
    description = models.TextField(max_length=5000)

    def __str__(self):
        return self.module_name

    class Meta:
        db_table = "Course_Modules"

class Enrollment(models.Model):
    student = models.ForeignKey(Students, on_delete=models.CASCADE)
    course = models.ForeignKey(Courses, on_delete=models.CASECADE)
    enrolled_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "enroll_details"
        unique_together = ("student", 'course')