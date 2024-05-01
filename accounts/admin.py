from django.contrib import admin
from .models import CustomUser,Profile


@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display=['email','is_customer','is_engineer','is_active','is_admin','is_staff']
    ordering=['email']

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display=['user','photo','joined_date']
    list_filter=['joined_date']
    ordering=['joined_date']