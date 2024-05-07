from django.shortcuts import render,redirect
from .forms import  CreateTicketForm,AssignTicketForm
from django.contrib.auth import get_user_model
from .models import Ticket
from django.contrib import messages
import random
import string
from django.db import IntegrityError
from django.core.mail import send_mail
User=get_user_model()
def create_ticket(request):
    if request.method =='POST':
        form=CreateTicketForm(request.POST)
        if form.is_valid():
            cd=form.save(commit=False)
            cd.customer=request.user
            while not cd.ticket_id:
                id=''.join(random.choices(string.digits, k=6))

                try:
                    cd.ticket_id=id
                    cd.save()
                    subject=f'{cd.ticket_title} - {cd.ticket_id}'
                    message='Thankyou for creating a ticket, we will assign an engineer soon'
                    email_from='admin@ticket.com'
                    recipient_list=[request.user.email]
                    send_mail(subject,message,email_from, recipient_list)
                    return redirect('customer-tickets')
                    # break
                except IntegrityError:
                    continue
            messages.success(request, 'Your ticket has been submitted, A support Engineer will reach out soon.')
            return redirect('customer-tickets')
        else:
            messages.warning(request, 'Something went wrong , please correc the error ')
            return redirect('create-ticket')
    else:
        form=CreateTicketForm()
        context={'form':form}
        return render(request, 'ticket/create_ticket.html',context)
    
def customer_active_tickets(request):
    tickets=Ticket.objects.filter(customer=request.user, is_resolved=False).order_by('created_on')
    context={'tickets':tickets}
    return render(request, 'ticket/customer_active_tickets.html',context)

def customer_resolved_tickets(request):
    tickets=Ticket.objects.filter(customer=request.user, is_resolved=True).order_by('created_on')
    context={'tickets',tickets}
    return render(request, 'ticket/customer_resolved_tickets.html',context)

def assign_ticket(request,ticket_id):
    ticket=Ticket.objects.get(ticket_id=ticket_id)
    if request.method == 'POST':
        form=AssignTicketForm(request.POST or None, instance=ticket)
        if form.is_valid():
            cd = form.save(commit=False)
            cd.is_assigned_to_engineer=True
            cd.save()
            messages.success(request, f'Ticket has been assigned to {cd.engineer}')
            return redirect('ticket-queue')
        else:
            messages.warning(request,'Please correc the error below')
            return redirect('assign-task')
        
    else:
        form=AssignTicketForm(instance=ticket)
        form.fields['engineer'].queryset=User.objects.filter(is_engineer=True)
        context={'form':form,'ticket':ticket}
        return render(request,'ticket/assign_ticket.html',context)

def ticket_details(request,ticket_id):
    ticket=Ticket.objects.get(ticket_id=ticket_id)
    context={'ticket':ticket}
    return render(request,'ticket/ticket_details.html', context)


def ticket_queue(request):
    tickets=Ticket.objects.filter(is_assigned_to_engineer=False)
    context={"tickets":tickets}
    return render(request,'ticket/ticket_queue.html', context)

def engineer_active_tickets(request):
    tickets=Ticket.objects.filter(engineer=request.user, is_resolved=False).order_by('-created_on')
    context={'tickets':tickets}
    return render(render, 'tickets/engineer_active_tickets.html',context)

def engineer_resolved_tickets(request):
    tickets=Ticket.objects.filter(engineer=request.user, is_resolved=True).order_by('-created_on')
    context={'tickets':tickets}
    return render(request, 'ticket/engineer_resolved_tickets.html', context)


def resolve_ticket(request, ticket_id):
    ticket=Ticket.objects.get(ticket_id=ticket_id)
    if request.method == 'POST':
        rs=request.POST.get('rs')
        ticket.resolution_steps=rs
        ticket.is_resolved=True
        ticket.status='Resolved'
        ticket.save()
        messages.success(request,"Ticket is now resolved and closed")
        return redirect('dashboard')