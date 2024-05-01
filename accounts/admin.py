from django.contrib import admin
from .models import CustomUser,Profile

admin.site.register(CustomUser)
# admin.site.register(Profile)
@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display=['user','photo','joined_date']
    list_filter=['joined_date']