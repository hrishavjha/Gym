from django.shortcuts import render

from services.models import Service


def prod_view(request, prod_id):
    user = request.user
    try:
        service = Service.objects.get(id=prod_id)
    except:
        service = None
    allService = Service.objects.all()
    context = {
        'title': service.name,
        'product': service,
        'allService': allService,
        'users': user,

    }
    return render(request, 'products/product.html', context)
