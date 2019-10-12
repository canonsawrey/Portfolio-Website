from django.urls import path

from . import views

app_name = 'home'
urlpatterns = [
    path('', views.home, name='home'),
    path('thanks/', views.thanks, name='thanks'),

    # Everything belo\w here deprecated
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact')
]
