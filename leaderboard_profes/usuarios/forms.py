from django import forms
from .models import *

class SubmitCourse(forms.ModelForm):

    class Meta:
        model = Course
        fields = '__all__'
