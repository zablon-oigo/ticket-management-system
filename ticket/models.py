from django.db import models
import uuid
from django.contrib.auth import get_user_model
from django.utils import timezone
User=get_user_model()
class Ticket(models.Model):
    status_choices=(
        ('Active','Active'),
        ('Completed','Completed'),
        ('Pending','Pending')
    )
    ticket_number=models.UUIDField(default=uuid.uuid4)
    title=models.CharField(max_length=100)
    description=models.TextField()
    created_by=models.ForeignKey(User,on_delete=models.CASCADE, related_name='created_by')
    date_created=models.DateTimeField(default=timezone.now)
    assigned_to=models.ForeignKey(User,on_delete=models.DO_NOTHING,null=True, blank=True)
    is_resolved=models.BooleanField(default=False)
    accepted_date=models.DateTimeField(null=True, blank=True)
    closed_date=models.DateTimeField(null=True,blank=True)
    ticket_status=models.CharField(max_length=15, choices=status_choices)

    class Meta:
        ordering=['-title']

    def __str__(self):
        return f'{self.title.capitalize()}'

