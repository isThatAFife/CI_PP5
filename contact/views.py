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
        form.save()
        send_mail(
            subject=f"New message from {form.cleaned_data['name']}",
            message=form.cleaned_data['message'],
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=[settings.NOTIFY_EMAIL],
            fail_silently=False,
        )
        messages.success(self.request, "Message received successfully!")
        return super().form_valid(form)
    
    
class ContactSuccessView(TemplateView):
    template_name = 'contact_success.html'