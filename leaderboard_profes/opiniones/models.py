from django.db import models
from usuarios.models import Course, Department, User

class Teacher(models.Model):
    teacher_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, null=False, blank=False)
    departments = models.ManyToManyField(Department)

    def __str__(self):
        return self.name

class Opinion(models.Model):
    DIFFICULTY_CHOICES = [(i, i) for i in range(1, 8)]
    THEORICITY_CHOICES = [(i, i) for i in range(1, 8)]
    MATRACA_CHOICES = [(i, i) for i in range(1, 8)]
    TEACHER_SUPPORT_CHOICES = [(i, i) for i in range(1, 8)]

    opinion_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.RESTRICT, null=False)
    course = models.ForeignKey(Course, on_delete=models.RESTRICT, null=False, verbose_name="Curso")
    professor = models.ForeignKey(Teacher, on_delete=models.RESTRICT, null=False, verbose_name="Profesor")
    course_date = models.DateField(auto_now_add=True, verbose_name="Fecha del curso")
    difficulty = models.PositiveIntegerField(choices=DIFFICULTY_CHOICES, verbose_name="Dificultad")
    theoricity = models.PositiveIntegerField(choices=THEORICITY_CHOICES, verbose_name="Teoricidad")
    matraca = models.PositiveIntegerField(choices=MATRACA_CHOICES)
    pauteable = models.BooleanField(null=False, blank=False)
    first_time = models.BooleanField(null=False, blank=False, verbose_name="Primera vez", default=False)
    teacher_support = models.PositiveIntegerField(choices=TEACHER_SUPPORT_CHOICES, verbose_name="Apoyo del profesor")



