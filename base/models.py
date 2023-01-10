from django.db import models

# Create your models here.

class Class(models.Model):
    pass

class Student(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField()

    class Meta:
        verbose_name = "Students"
        verbose_name_plural = "Students"

    def __str__(self):
        return self.name