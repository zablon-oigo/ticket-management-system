from django.contrib import admin
from .models import CustomUser,Profile

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display=['user','photo','date_joined']
    list_filter=['date_joined']
