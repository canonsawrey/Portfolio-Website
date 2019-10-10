from django.shortcuts import render


def home(request):
    return render(request, 'home/home.html')


def bio(request):
    return render(request, 'home/bio.html')


def contact(request):
    return render(request, 'home/contact.html')

