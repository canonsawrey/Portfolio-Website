from django.shortcuts import render, get_object_or_404
from .models import Job


def index(request):
    job_list = Job.objects.order_by('-start_date')
    context = {'job_list': job_list}
    return render(request, 'jobs/index.html', context)


def detail(request, project_id):
    job = get_object_or_404(Job, pk=project_id)
    return render(request, 'jobs/detail.html', {'job': job})
