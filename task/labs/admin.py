from django.contrib import admin
from .models import *
from django.contrib.auth.admin import UserAdmin

# Register your models here.
admin.site.register(Bloodtest)
admin.site.register(Livertest)
admin.site.register(UserProfile)