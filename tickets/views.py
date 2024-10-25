# # tickets/views.py
# from django.shortcuts import render, get_object_or_404, redirect
# from django.contrib.auth.mixins import LoginRequiredMixin
# from django.views.generic import ListView, CreateView, DetailView
# from django.contrib import messages
# from django.urls import reverse_lazy
# from django.utils import timezone
# from .models import Ticket, TicketChat, Message
# from .forms import TicketForm, TicketChatForm, MessageForm
# from django.views import View
# from django.utils.decorators import method_decorator
# from django.contrib.auth.decorators import login_required

# class TicketCreateView(CreateView):
#     model = Ticket
#     form_class = TicketForm
#     template_name = 'tickets/ticket_form.html'
#     success_url = reverse_lazy('home')

#     def form_valid(self, form):
#         form.instance.user = self.request.user
#         form.instance.user_agent = self.request.META.get('HTTP_USER_AGENT', 'unknown')
#         form.instance.page_url = self.request.META.get('HTTP_REFERER', 'unknown')
#         response = super().form_valid(form)
#         messages.success(self.request, f'Ticket "{form.cleaned_data["title"]}" creado con éxito.')
#         return response

# class TicketListView(LoginRequiredMixin, ListView):
#     model = Ticket
#     template_name = 'tickets/ticket_list.html'
#     context_object_name = 'tickets'

#     def get_queryset(self):
#         queryset = Ticket.objects.filter(user=self.request.user).order_by('-created_at')
#         ticket_type = self.request.GET.get('ticket_type')
#         status = self.request.GET.get('status')
        
#         if ticket_type:
#             queryset = queryset.filter(ticket_type=ticket_type)
#         if status:
#             if status == 'resolved':
#                 queryset = queryset.filter(is_resolved=True)
#             elif status == 'unresolved':
#                 queryset = queryset.filter(is_resolved=False)
#             elif status == 'all':
#                 queryset = queryset
                
#         return queryset

# @method_decorator(login_required, name='dispatch')
# class TicketDetailView(View):
#     template_name = 'tickets/ticket_detail.html'

#     def get(self, request, pk, *args, **kwargs):
#         ticket = get_object_or_404(Ticket, pk=pk)
#         chats = TicketChat.objects.filter(ticket=ticket).order_by('timestamp')
#         form = TicketChatForm()
#         return render(request, self.template_name, {'ticket': ticket, 'chats': chats, 'new_message_form': form})

#     def post(self, request, pk, *args, **kwargs):
#         ticket = get_object_or_404(Ticket, pk=pk)
#         form = TicketChatForm(request.POST)
#         if form.is_valid():
#             chat = form.save(commit=False)
#             chat.ticket = ticket
#             chat.user = request.user
#             chat.save()
#             return redirect('ticket_detail', pk=ticket.pk)
#         chats = TicketChat.objects.filter(ticket=ticket).order_by('timestamp')
#         return render(request, self.template_name, {'ticket': ticket, 'chats': chats, 'new_message_form': form})

# class TicketChatCreateView(LoginRequiredMixin, CreateView):
#     model = TicketChat
#     form_class = TicketChatForm
#     template_name = 'tickets/ticket_detail.html'

#     def form_valid(self, form):
#         form.instance.user = self.request.user
#         form.instance.ticket = get_object_or_404(Ticket, pk=self.kwargs['pk'])
#         response = super().form_valid(form)
#         messages.success(self.request, 'Mensaje enviado.')
#         return redirect('ticket_detail', pk=self.kwargs['pk'])

# class MarkTicketResolvedView(LoginRequiredMixin, DetailView):
#     model = Ticket

#     def get(self, request, *args, **kwargs):
#         ticket = self.get_object()
#         ticket.is_resolved = True
#         ticket.updated_at = timezone.now()
#         ticket.save()
#         messages.success(request, 'Ticket marcado como resuelto.')
#         return redirect('ticket_list')


# class MarkTicketUnresolvedView(LoginRequiredMixin, DetailView):
#     model = Ticket

#     def get(self, request, *args, **kwargs):
#         ticket = self.get_object()
#         ticket.is_resolved = False
#         ticket.updated_at = timezone.now()
#         ticket.save()
#         messages.success(request, 'Ticket marcado como no resuelto.')
#         return redirect('ticket_list')