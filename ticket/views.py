from django.shortcuts import render,redirect
from .forms import  CreateTicketForm
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
    tickets=Ticket.objects.filter(customer=request.user)
    context={'tickets',tickets}
    return render(request, 'ticket/customer_tickets.html',context)
