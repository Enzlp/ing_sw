from django import forms
from .models import *

class SubmitOpinion(forms.ModelForm):
    class Meta:
        model = Opinion
        fields = ['course', 'professor', 'difficulty', 'theoricity', 'matraca', 'pauteable', 'teacher_support']
