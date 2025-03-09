from django.shortcuts import render
from django.http import HttpResponse

def contact_view(request):
    try:
        return render(request, 'contact/contact.html')
    except Exception as e:
        return HttpResponse(f"Error: {e}")