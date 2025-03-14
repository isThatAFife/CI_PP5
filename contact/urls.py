from django.urls import path
from .views import ContactFormView, ContactSuccessView

urlpatterns = [
    path('', ContactFormView.as_view(), name='contact'),
    path('', ContactSuccessView.as_view(), name='contact_success'),
]
