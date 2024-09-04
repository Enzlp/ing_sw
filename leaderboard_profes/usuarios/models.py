from django.db import models

from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import User

class Major(models.Model):
    major_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50, blank=False, null=False)

    def __str__(self):
        return self.name

class Department(models.Model):
    department_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50, blank=False, null=False)

    def __str__(self):
        return self.name
    
class User(AbstractUser):
    pass

class UcampusUser(models.Model):
    id = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    major = models.ForeignKey(Major, on_delete=models.RESTRICT, null=False)
    ucampus_login = models.CharField(max_length=255, blank=False, null=False)

class Course(models.Model):
    course_id = models.AutoField(primary_key=True) 
    code = models.CharField(max_length=30, unique=True, blank=False, null=False, verbose_name="Código")
    name = models.CharField(max_length=255, verbose_name="Nombre")
    department = models.ForeignKey(Department, on_delete=models.RESTRICT, null=False, verbose_name="Departamento")
    credits = models.PositiveIntegerField()

    @property
    def avg_difficulty(self):
        avg = self.opinion_set.aggregate(models.Avg('difficulty'))['difficulty__avg']
        return avg if avg else 'N/A'

    @property
    def avg_theoricity(self):
        avg = self.opinion_set.aggregate(models.Avg('theoricity'))['theoricity__avg']
        return avg if avg else 'N/A'
    @property
    def avg_matraca(self):
        avg = self.opinion_set.aggregate(models.Avg('matraca'))['matraca__avg']
        return avg if avg else 'N/A'
    @property
    def avg_teacher_support(self):
        avg = self.opinion_set.aggregate(models.Avg('teacher_support'))['teacher_support__avg']
        return avg if avg else 'N/A'

    def __str__(self):
        return f'{self.code} - {self.name}'
