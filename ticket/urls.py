from django.urls import path
from .views import (ticket_details,ticket_queue,create_ticket,assign_ticket ,\
                    customer_active_tickets,customer_resolved_tickets,engineer_active_tickets,engineer_resolved_tickets)

urlpatterns=[
    path('create-ticket/', create_ticket, name='create_ticket'),
    path('customer-tickets/', customer_active_tickets, name='customer-tickets'),
    path('customer-resolved-tickets/', customer_resolved_tickets, name='resolved'),
    path('assign-ticket/<str:ticket_id>/', assign_ticket, name='assign-ticket'),
    path('ticket-details/<str:ticket_id>/', ticket_details, name='ticket-details'),
    path('ticket-queue/', ticket_queue, name='ticket-queue'),
    path('engineer-active/', engineer_active_tickets, name='engineer-active'),
    path('engineer-resolved/', engineer_resolved_tickets, name='engineer-resolved'),
]