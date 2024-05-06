from django import forms
from .models import Ticket

class CreateTicketForm(forms.ModelForm):
    class Meta:
        model=Ticket
        fields=['ticket_title','ticket_description']
    ticket_title=forms.CharField( label='ticket title',widget=forms.TextInput(
            attrs={
                'class':'px-6 py-4 w-full rounded-xl mb-2'
            }

    ))
    ticket_description=forms.CharField( label='ticket description',widget=forms.Textarea(
        attrs={
            'class':'px-6 py-4 w-full rounded-xl mb-2'
        }
    ))


class AssignTicketForm(forms.ModelForm):
    class Meta:
        model=Ticket
        fields=['engineer']