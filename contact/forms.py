from django import forms
from .models import ContactMessage
from django.core.validators import MinLengthValidator
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Field, Submit

class ContactForm(forms.ModelForm):
    name = forms.CharField(
        validators=[MinLengthValidator(2, "Name must be at least 2 characters")],
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    
    message = forms.CharField(
        validators=[MinLengthValidator(10, "Message must be at least 10 characters")],
        widget=forms.Textarea(attrs={
            'rows': 8,
            'class': 'tall-message-field form-control',
            'style': 'min-height:150px;'
        })
    )

    class Meta:
        model = ContactMessage
        fields = ['name', 'email', 'subject', 'message']
        widgets = {
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'subject': forms.TextInput(attrs={'class': 'form-control'}),
            'message': forms.Textarea(attrs={'rows': 5, 'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.layout = Layout(
            Field('name', css_class='col-md-6 mb-3'),
            Field('email', css_class='col-md-6 mb-3'),
            Field('subject', css_class='col-md-6 mb-3'),
            Field('message', css_class='tall-message-field mb-3'),
            Submit('submit', 'Send', css_class='btn-primary')
        )
        self.helper.label_class = 'text-left col-form-label'
