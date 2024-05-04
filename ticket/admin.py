from django.contrib import admin
from .models import Ticket

@admin.register(Ticket)
class TicketAdmin(admin.ModelAdmin):
    list_display=['customer','engineer','status','created_on','is_resolved','severity','is_assigned_to_engineer']
    list_filter=['created_on','is_resolved','status']
    