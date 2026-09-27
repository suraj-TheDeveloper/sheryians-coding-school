from django.db import models

# Create your models here.
class Courses(models.Model):
    title = models.CharField(max_length=500)
    duration = models.CharField(max_length=100)
    price = models.IntegerField()
    description = models.TextField(max_length = 2000)

    def __str__(self):
        return self.title

    class Meta:
        db_table = "Courses"