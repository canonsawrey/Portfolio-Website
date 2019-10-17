from django.http import HttpResponseRedirect
from django.shortcuts import render
from home.forms import ContactForm
from django.core.mail import send_mail


def home(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)

        if form.is_valid():

            send_mail(
                subject='Website Contact Form',
                message=get_details(request),
                from_email="Personal Website",
                recipient_list=["sawrey.c@husky.neu.edu"]
            )

            return HttpResponseRedirect('/thanks/')

    else:
        form = ContactForm()

    return render(request, 'home/home.html', {'form': form})


def get_details(request):
    return_string = "".join(
        ["First: ", request.POST.get('first_name'),
         "\nLast: ", request.POST.get('last_name'),
         "\nEmail: ", request.POST.get('email'),
         "\nContent: ", request.POST.get('content')])
    return return_string


def about(request):
    return render(request, 'home/home.html')


def contact(request):
    return render(request, 'home/contact.html')


def thanks(request):
    return render(request, 'home/thanks.html')
