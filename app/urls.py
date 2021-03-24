from django.urls import path
from django.contrib.auth import views as auth_views

from app import views

urlpatterns = [
    # The home page
    path('', views.Index, name='Index'),
    
]