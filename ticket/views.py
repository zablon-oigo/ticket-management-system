from django.shortcuts import render,redirect
from .forms import  CreateTicketForm,AssignTicketForm
from .models import Ticket
from django.contrib import messages
import random
import string
from django.db import IntegrityError

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
                    break
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
    
def customer_tickets(request):
    tickets=Ticket.objects.filter(customer=request.user, is_resolved=False).order_by('created_on')
    context={'tickets',tickets}
    return render(request, 'ticket/customer_tickets.html',context)

def customer_resolved_tickets(request):
    tickets=Ticket.objects.filter(customer=request.user, is_resolved=True).order_by('created_on')
    context={'tickets',tickets}
    return render(request, 'ticket/customer_tickets.html',context)

def assign_ticket(request,ticket_id):
    ticket=Ticket.objects.get(ticket_id=ticket_id)
    if request.method == 'POST':
        form=AssignTicketForm(request.POST, instance=ticket)
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
        form=AssignTicketForm()
        context={'form':form}
        return render(request,'ticket/assign_ticket.html',context)

def ticket_details(request,ticket_id):
    ticket=Ticket.objects.get(ticket_id=ticket_id)
    context={'ticket':ticket}
    return render(request,'ticket/ticket_detail.html', context)


def ticket_queue(request):
    tickets=Ticket.objects.filter(is_assigned_to_engineer=False)
    context={"tickets":tickets}
    return render(request,'ticket/tikcet_queue.html', context)