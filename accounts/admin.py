from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

# Register your models here.

class CustomUserAdmin(UserAdmin):
	list_display = ('email', 'first_name', 'last_name','phone_number',)
	filter_horizontal = ()
	list_filter = ()
	fieldsets = ()
	ordering = ('-date_joined',)

admin.site.register(CustomUser, CustomUserAdmin)