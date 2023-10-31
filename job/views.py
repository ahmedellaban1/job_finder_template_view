from django.shortcuts import render
from .models import Job
from django.shortcuts import get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def job_list(request):
    query = Job.objects.all()
    jobs_count = query.count()
    page = request.GET.get('page', 1)
    paginator = Paginator(query, 50)
    try:
        query = paginator.page(page)
    except PageNotAnInteger:
        query = paginator.page(1)
    except EmptyPage:
        query = paginator.page(paginator.num_pages)
    context = {
        'jobs': query,
        'jobs_count': jobs_count,
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
