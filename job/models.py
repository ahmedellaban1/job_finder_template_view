from django.db import models
from django.utils import timezone
from etc.choices import JOB_TYPE
from etc.file_uploader import company_image_uploader, category_logo_uploader
# TODO: install django-countries

class Job(models.Model):
    title = models.CharField(max_length=120)
    # location = C
    company = models.ForeignKey('Company', on_delete=models.CASCADE, related_name='job_company')
    created_at = models.DateTimeField(default=timezone.now)
    salary_start = models.IntegerField(null=True, blank=True)
    salary_end = models.IntegerField(null=True, blank=True)
    description = models.TextField(max_length=15000)
    vacancy = models.IntegerField()
    job_type = models.CharField(choices=JOB_TYPE, default=JOB_TYPE[4][0], max_length=10)
    experience = models.IntegerField()
    category = models.ForeignKey('Category', null=True, blank=True, on_delete=models.SET_NULL, related_name='job_category')

class Category(models.Model):
    name = models.CharField(max_length=30)
    logo = models.ImageField(upload_to=category_logo_uploader)


class Company(models.Model):
    name = models.CharField(max_length=20)
    logo = models.ImageField(upload_to=company_image_uploader, null=True, blank=True)
    subtitle = models.TextField(max_length=1000)
    website = models.URLField()
    email = models.EmailField()
