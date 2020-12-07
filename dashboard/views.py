from django.contrib.auth import login
from django.shortcuts import render


def dash_view(request):
    context = {
        'title': 'Dashboard',
    }
    return render(request, 'dashboard/dash.html', context)
