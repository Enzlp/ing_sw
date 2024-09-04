from django.urls import path
from . import views
from usuarios.views import landing_page

app_name = 'opiniones'

urlpatterns = [
    path('', landing_page, name='main'),
    path('opinion-form', views.opinion_form, name='opinion-form'),
    path('opinion-list', views.opinion_list, name='opinion-list'),
]