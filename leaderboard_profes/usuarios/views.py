from django.shortcuts import redirect, render
from django.http import HttpResponseRedirect
from usuarios.models import *
from django import views
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.contrib.auth import authenticate, login, logout
from .forms import SubmitCourse
from opiniones.views import opinion_form
# Create your views here.

def landing_page(request):
   if request.method == "GET":
      return render(request, "usuarios/index.html")

def register_user(request):
   if request.method == 'GET': 
     return render(request, "usuarios/register_user.html")
   elif request.method == 'POST': 
     nombre = request.POST['nombre']
     contraseña = request.POST['contraseña']
     mail = request.POST['mail']
     user = User.objects.create_user(username=nombre, password=contraseña, email=mail)
     return HttpResponseRedirect('/login')
   
def login_user(request):
    if request.method == 'GET':
        return render(request,"usuarios/login_user.html")
    if request.method == 'POST':
        username = request.POST['username']
        contraseña = request.POST['contraseña']
        usuario = authenticate(username=username,password=contraseña)
        if usuario is not None:
            login(request, usuario)
            return HttpResponseRedirect(reverse_lazy('opiniones:opinion-form'))
        else:
            return HttpResponseRedirect(reverse_lazy('usuarios:register_user'))

class ProfileView(LoginRequiredMixin,views.View):
   login_url = reverse_lazy("login")
   redirect_field_name = "redirect_to"
   
   def get(self,request):
      context = {
         'user': request.user
      }
      return render(request, 'usuarios/profile.html',context)

def list_cursos(request):
   courses = Course.objects.all()
   return render(request,"usuarios/list_cursos.html", {'cursos':courses})

def create_curso(request):
   if request.method == "POST":
      form = SubmitCourse(request.POST)
      if form.is_valid():
         form.save()
         # send to list_cursos
         return redirect('usuarios:cursos-list')
   form = SubmitCourse()
   return render(request,"usuarios/create_curso.html", {'forms':form})

def view_curso(request, pk):
   curso = Course.objects.get(pk=pk)
   return render(request,"usuarios/view_curso.html", {'curso':curso})