from django.contrib import admin
from django.urls import path
from django.contrib.auth.views import LogoutView
from django.conf.urls.static import static
from django.conf import settings

from services.views import service_view
from home.views import home_view, about_view, work_view, contact_view
from account.views import login_view, register_view
from dashboard.views import dash_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_view, name='home'),
    path('about/', about_view, name='about'),
    path('work/', work_view, name='work'),
    path('contact/', contact_view, name='contact'),
    path('login/', login_view, name='login'),
    path('register/', register_view, name='register'),
    path('services/', service_view, name='services'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('dashboard/', dash_view, name='dashboard'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
