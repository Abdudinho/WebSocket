from django.db import models
from django.db.models.fields import CharField


class Category(models.Model):
    title = CharField(max_length=255)

class Student(models.Model):
    photo = models.ImageField(upload_to="photos/", blank=True, null=True)
    fullname = models.CharField(max_length=255)

    def __str__(self):
        return self.fullname

class Ball(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='balls')
    coin = models.IntegerField()

    def __str__(self):
        return self.student.fullname