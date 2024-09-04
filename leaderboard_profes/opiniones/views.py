from django.shortcuts import redirect, render

from opiniones.models import Opinion
from .forms import SubmitOpinion
from usuarios.models import Course
# Create your views here.

def main(request):
   return render(request,"opiniones/base_layout.html")

def opinion_form(request):
   if request.method == "POST":
      form = SubmitOpinion(request.POST)
      if form.is_valid():
         opinion = form.save(commit=False)
         opinion.user = request.user
         opinion.save()
         return redirect('usuarios:cursos-view', pk=opinion.course.pk)
   curso_id = request.GET.get('curso_id')
   if curso_id:
      print('curso id')
      course = Course.objects.get(pk=curso_id)
      form = SubmitOpinion(initial={'course':curso_id})
   else:
      form = SubmitOpinion()
   return render(request,"opiniones/opinion_form.html", {'forms':form})

def opinion_list(request):
   opiniones = Opinion.objects.all()
   return render(request,"opiniones/opinion_list.html", {'opiniones':opiniones})