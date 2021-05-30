from django.contrib import admin

# Register your models here.
from .models import Student, User, EventRegistration
from .models import *


admin.site.register(Student)

admin.site.register(User)


admin.site.register(EventRegistration)

admin.site.register(valorant_registration)

admin.site.register(csgo_registration)
