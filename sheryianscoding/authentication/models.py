from django.db import models

# Create your models here.
class Students(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    phone = models.IntegerField()
    email = models.EmailField()

    def __str__(self):
        return self.first_name

    class Meta:
        db_table = 'Students'