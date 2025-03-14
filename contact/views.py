from django.views.generic import FormView, TemplateView
from django.urls import reverse_lazy
from .forms import ContactForm
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings

class ContactFormView(FormView):
    form_class = ContactForm
    template_name = 'contact/contact.html'
    success_url = reverse_lazy('contact_success')

    def form_valid(self, form):
        # Save to database
        message = form.save()
        
        # Send email notification
        send_mail(
            subject=f"New Contact: {message.subject}",
            message=f"From: {message.name} <{message.email}>\n\n{message.message}",
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=[settings.DEFAULT_FROM_EMAIL],
            fail_silently=False,
        )
        
        messages.success(self.request, "Message received successfully!")
        return super().form_valid(form)
    
    
class ContactSuccessView(TemplateView):
    template_name = 'contact/contact_success.html'