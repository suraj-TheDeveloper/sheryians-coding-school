from django.db import models

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
    student = models.ForeignKey('authentication.Students', on_delete=models.CASCADE)
    course = models.ForeignKey(Courses, on_delete=models.CASCADE)
    enrolled_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "enroll_details"
        unique_together = ("student", 'course')

class Payments(models.Model):
    STATUS_CHOICES = [
        ("pending", "Pending"),
        ("success", "Success"),
        ("failed", "Failed"),
    ]
    CARD_CHOICES = [
        ("visa", "Visa"),
        ("mastercard", "Mastercard"),
        ("rupay", "RuPay"),
        ("other", "Other")
    ]
    student = models.ForeignKey('authentication.Students', on_delete=models.CASCADE)
    course = models.ForeignKey(Courses, on_delete=models.CASCADE)
    enrollid = models.ForeignKey(Enrollment, on_delete=models.CASCADE)
    transactionid = models.CharField(max_length=50, unique=True)
    amount = models.IntegerField()
    status = models.CharField(max_length=15, choices=STATUS_CHOICES, default="pending")
    card_holder_name = models.CharField(max_length=100)
    card_last4 = models.CharField(max_length=4)
    card_type = models.CharField(max_length=50, choices=CARD_CHOICES, blank=True)

    class Meta:
        db_table = "payments"