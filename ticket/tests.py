from django.test import TestCase
from .models import Ticket
from django.contrib.auth import get_user_model
from django.urls import reverse
class TicketTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        User = get_user_model()
        cls.customer= User.objects.create_user(email="normal@user.com", password="secret")
        cls.engineer= User.objects.create_user(email="engineer@user.com", password="secret")
        cls.ticket=Ticket.objects.create(
            ticket_title="ticket 1",
            ticket_description="linux server installation",
            is_resolved=False,
            status="Pending",
            customer=cls.customer,
            engineer=cls.engineer
        )

    def test_model_content(self):
        self.assertEqual(self.ticket.ticket_title,"ticket 1")
        self.assertEqual(self.ticket.ticket_description,"linux server installation")
        self.assertEqual(self.ticket.is_resolved,False)
        self.assertEqual(Ticket.objects.count(),1)
        self.assertEqual(str(self.ticket),"ticket 1")

    def test_create_ticket_view(self):
        self.client.force_login(self.customer)
        response=self.client.post(reverse("create_ticket"),{
            "ticket_title":"windows os",
            "ticket_description":"windows installation",
            "status":"Pending",
        })
        self.assertEqual(response.status_code,302)
        self.assertEqual(Ticket.objects.last().ticket_title,"windows os")
        self.assertEqual(Ticket.objects.last().ticket_description,"windows installation")
        
    def test_ticket_detail(self):
        response=self.client.get(reverse("ticket-details"), kwargs={
            "pk":self.ticket.pk
        })
        self.assertEqual(response.status_code, 200)
        