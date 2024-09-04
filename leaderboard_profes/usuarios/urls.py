from django.urls import path
from . import views

app_name = 'usuarios'

urlpatterns = [
    path('register', views.register_user, name='register_user'), 
    path('login',views.login_user, name='login'),
    path('profile',views.ProfileView.as_view(), name = 'profile'),
    path('cursos', views.list_cursos, name='cursos-list'),
    path('cursos/crear', views.create_curso, name='cursos-create'),
    path('cursos/<int:pk>/', views.view_curso, name='cursos-view'),
    path('landing_page', views.landing_page, name = 'landing_page')
]