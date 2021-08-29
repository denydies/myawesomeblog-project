from django.shortcuts import render
from .models import Event


def home_page(request):
    events = Event.objects.all()
    return render(request, 'events/home_page.html', {'events': events})
