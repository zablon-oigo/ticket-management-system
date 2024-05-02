from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser,Profile
from .forms import CustomUserCreationForm, CustomUserChangeForm

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ("email", "is_staff", "is_active",)
    list_filter = ("email", "is_staff", "is_active",)
    fieldsets = (
        (None, {"fields": ("email", "password")}),
        ("Permissions", {"fields": ("is_staff", "is_active","groups", "user_permissions")}),
    )
    add_fieldsets = (
        (None, {
            "classes": ("wide",),
            "fields": (
                "email", "password1", "password2", "is_staff",
                "is_active","is_engineer","is_customer","groups", "user_permissions"
            )}
        ),
    )
    search_fields = ("email",)
    ordering = ("email",)


admin.site.register(CustomUser, CustomUserAdmin)
# @admin.register(CustomUser)
# class CustomUserAdmin(admin.ModelAdmin):
#     list_display=['email','is_customer','is_engineer','is_active','is_admin','is_staff']
#     ordering=['email']

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display=['user','photo','joined_date']
    list_filter=['joined_date']
    ordering=['joined_date']