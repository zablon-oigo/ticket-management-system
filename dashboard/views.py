from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from ticket.models import Ticket
@login_required
def dashboard(request):
    if request.user.is_customer:
        tickets=Ticket.objects.filter(customer=request.user)
        active_tickets=Ticket.objects.filter(customer=request.user, is_resolved=False).count
        closed_tickets=Ticket.objects.filter(customer=request.user, is_resolved=True).count
        context={
            'tickets':tickets,
            'active_tickets':active_tickets,
            'closed_tickets':closed_tickets,
            }
        return render(request,'dashboard/customer_dashboard.html',context)
    elif request.user.is_engineer:
        tickets=Ticket.objects.filter(engineer=request.user)
        active_tickets=Ticket.objects.filter(engineer=request.user, is_resolved=False).count
        closed_tickets=Ticket.objects.filter(engineer=request.user, is_resolved=True).count
        context={
            'tickets':tickets,
            'active_tickets':active_tickets,
            'closed_tickets':closed_tickets,
        }
        return render(request, 'dashboard/engineer_dashboard.html')
    
    elif request.user.is_superuser:
        tickets=Ticket.objects.filter(is_assigned_to_engineer=False)
        context={"tickets":tickets}
        return render(request, 'dashboard/admin_dashboard.html',context)
