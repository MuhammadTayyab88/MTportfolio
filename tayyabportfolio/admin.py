from django.contrib import admin

# Register your models here.
# admin.py
from .models import *

@admin.register(CV)
class CVAdmin(admin.ModelAdmin):
    list_display = ('file',)  # Display the file in the admin list view


class ProfileAdmin(admin.ModelAdmin):
    list_display = ['id', 'profile_image']  # Customize as needed

admin.site.register(Profile, ProfileAdmin)




admin.site.register(Skills)