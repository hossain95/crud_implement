from django.db import models


# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    semester = models.CharField(max_length=12)

    def __str__(self):
        return self.name
