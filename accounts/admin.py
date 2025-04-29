from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import CustomUserCreationForm,CustomUserChangeForm
from .models import CustomUser

# Register your models here.

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ['id', 'username','email','mobile',]
    fieldsets = UserAdmin.fieldsets +  ((None,  {'fields': ('mobile', 'avatar', 'bio', 'dob', 'gender',)}),)
    
admin.site.register(CustomUser, CustomUserAdmin)