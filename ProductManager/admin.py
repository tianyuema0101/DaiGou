from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
from .models import *

# Register your models here.
# Re-register UserAdmin
#admin.site.register(User)
#admin.site.register(User, UserAdmin)

admin.site.register(Product)
admin.site.register(Image)
admin.site.register(Category)