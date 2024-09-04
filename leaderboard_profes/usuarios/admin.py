from django.contrib import admin
from usuarios.models import *

# Modificaciones al Codigo:
from usuarios.models import User

# Register your models here.
admin.site.register(Course)
admin.site.register(Department)
admin.site.register(User)