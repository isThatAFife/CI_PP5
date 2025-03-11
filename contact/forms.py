from django import forms
from .models import ContactMessage
from django.core.validators import MinLengthValidator

class ContactForm(forms.ModelForm):
    name = forms.CharField(
        validators=[MinLengthValidator(2, "Name must be at least 2 characters")]
    )
    message = forms.CharField(
        validators=[MinLengthValidator(10, "Message must be at least 10 characters")]
    )
    
    class Meta:
        model = ContactMessage
        fields = ['name', 'email', 'subject', 'message']
        widgets = {
            'message': forms.Textarea(attrs={'rows': 5}),
        }