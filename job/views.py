from django.shortcuts import render
from .models import Job, JobApply
from django.shortcuts import get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic import CreateView
from .forms import JobApplyForm, CreateJobForm

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


class JopApplyView(CreateView):
    model = JobApply
    success_url = '/'
    # fields = ['email', 'linkedIn', 'github', 'cv', 'cover_litter']
    template_name = 'job/apply_job.html'
    form_class = JobApplyForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["page_title"] = f'Apply Job | {self.kwargs["slug"]}'
        return context

    def form_valid(self, form):
        job = get_object_or_404(Job, slug=self.kwargs['slug'], id=self.kwargs['id'])
        job_apply = form.save(commit=False)
        job_apply.job = job
        job_apply.save()
        return super().form_valid(form)


class CreateJobView(CreateView):
    model = Job
    form_class = CreateJobForm
    success_url = '/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["page_title"] = 'Create New Job'
        return context
