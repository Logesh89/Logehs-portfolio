from django.urls import path
from . import views

urlpatterns = [
    path('', views.default, name='default'),
    path('home/', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('myresume/', views.myresume, name='myresume'),
]