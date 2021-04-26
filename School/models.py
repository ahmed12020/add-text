from django.db import models
from .managers import CustomManager
from ckeditor.fields import RichTextField

# Create your models here.


class Student(models.Model):
    name = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    body = RichTextField()
    objects = models.Manager()

    def __str__(self):
        return self.name




# class ProxyStudent(Student):
#     students = CustomManager()
#     class Meta:
#         Proxy = True
#         ordering = ['name']





class Score(models.Model):
    result = models.PositiveIntegerField()

    def __str__(self):
        return str(self.result)




















