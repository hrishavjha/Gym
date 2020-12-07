from django.shortcuts import render

from .models import Service


def service_view(request):
    services = Service.objects.all()
    context = {
        'title': 'Services',
        'services': services
    }
    return render(request, 'services/service.html', context)
