from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Sample


def index(request):
    sample_list = Sample.objects.order_by('-start_date')
    context = {'sample_list': sample_list}
    return render(request, 'samples/index.html', context)


def detail(request, sample_id):
    sample = get_object_or_404(Sample, pk=sample_id)
    return render(request, 'samples/detail.html', {'sample': sample})

