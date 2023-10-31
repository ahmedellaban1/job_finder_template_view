from django.urls import path
from .views import job_list, job_details, JopApplyView, CreateJobView

urlpatterns = [
    path('', job_list, name='job_list'),
    path('create/', CreateJobView.as_view(), name='create_job'),
    path('<str:slug>-<int:id>', job_details, name='job_details'),
    path('<str:slug>-<int:id>/apply', JopApplyView.as_view(), name='job_apply'),
]
