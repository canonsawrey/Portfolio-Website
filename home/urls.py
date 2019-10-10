from django.urls import path

from . import views

app_name = 'home'
urlpatterns = [
    path('', views.home, name='home'),
    path('bio/', views.bio, name='bio'),
    path('contact/', views.contact, name='contact')
]
