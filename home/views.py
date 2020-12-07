from django.shortcuts import render


def home_view(request):
    context = {
            'title': 'Home',
        }
    return render(request, 'home/home.html', context)


def about_view(request):
    context = {
        'title': 'About',
    }
    return render(request, 'home/about.html', context)


def work_view(request):
    context = {
        'title': 'Work',
    }
    return render(request, 'home/work.html', context)


def contact_view(request):
    context = {
        'title': 'Contact Us',
    }
    return render(request, 'home/contact.html', context)
