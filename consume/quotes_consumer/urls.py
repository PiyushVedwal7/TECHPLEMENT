# quotes_consumer/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('quote/', views.display_quote, name='display_quote'),
]
