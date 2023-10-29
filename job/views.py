from django.shortcuts import render
from .models import Job
from django.shortcuts import get_object_or_404


def job_list(request):
    query = Job.objects.all()
    context = {
        'jobs': query,
        'page_title': 'Find Job',
    }
    return render(request, 'job/job_list.html', context)


def job_details(request, **kwargs):
    job = get_object_or_404(Job, slug=kwargs['slug'], id=kwargs['id'])
    context = {
        'page_title': f"{job.slug}",
        'job': job
    }
    return render(request, 'job/job_details.html', context)
