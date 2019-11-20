# from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.urls import path, include

urlpatterns = [
    # APIs
    path('services/', include('services.api.urls', namespace='services')),
    path('hosts/', include('hosts.api.urls', namespace='hosts')),
]
