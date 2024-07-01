# consume/urls.py
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('quotes_consumer/', include('quotes_consumer.urls')),
]
