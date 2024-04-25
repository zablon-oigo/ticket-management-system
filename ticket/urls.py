from django.urls import path
from .views import (ticket_details,ticket_queue,create_ticket,assign_ticket ,customer_tickets)

urlpatterns=[
    path('create-ticket/', create_ticket, name='create_ticket'),
    path('customer-tickets/', customer_tickets, name='customer-tickets'),
    path('assign-ticket/<str:ticket_id>/', assign_ticket, name='assign-ticket'),
    path('ticket-details/<str:ticket_id>/', ticket_details, name='ticket-details'),
    path('ticket-queue/', ticket_queue, name='ticket-queue'),
]