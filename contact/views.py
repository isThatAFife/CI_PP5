from django.views.generic import FormView
from django.urls import reverse_lazy
from .forms import ContactForm
from django.contrib import messages

class ContactFormView(FormView):
    form_class = ContactForm
    template_name = 'contact.html'
    success_url = reverse_lazy('contact_success')

    def form_valid(self, form):
        form.save()
        messages.success(self.request, "Message received successfully!")
        return super().form_valid(form)