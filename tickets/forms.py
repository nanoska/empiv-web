# tickets/forms.py
from django import forms
from .models import Ticket, TicketChat, Message

class TicketForm(forms.ModelForm):

    user_agent = forms.CharField(widget=forms.HiddenInput(), required=False)
    page_url = forms.CharField(widget=forms.HiddenInput(), required=False)

    class Meta:
        model = Ticket
        fields = ['title', 'description', 'ticket_type', 'user_agent', 'page_url']
        widgets = {
            'title': forms.TextInput(attrs={'placeholder': 'Título'}),
            'description': forms.Textarea(attrs={'placeholder': 'Descripción'}),
            'ticket_type': forms.Select(attrs={'placeholder': 'Tipo de Ticket'}),
        }

class TicketChatForm(forms.ModelForm):
    class Meta:
        model = TicketChat
        fields = ['message']
        widgets = {
            'message': forms.Textarea(attrs={'placeholder': 'Escribe tu mensaje aquí...', 'rows': 3}),
        }

class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ['content']
        widgets = {
            'content': forms.Textarea(attrs={'placeholder': 'Escribe tu mensaje aquí...'}),
        }
