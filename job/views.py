from django.shortcuts import render
from .models import Job


def job_list(request):
    query = Job.objects.all()
    context = {
        'jobs': query,
        'page_title': 'Find Job',
    }
    return render(request, 'job/job_list.html', context)
