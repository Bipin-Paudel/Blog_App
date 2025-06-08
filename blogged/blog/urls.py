from . import views
from django.urls import path, include

urlpatterns = [
    path('<slug:slug>', views.detail, name='detail'),
    path('', views.Home, name='home')
]
