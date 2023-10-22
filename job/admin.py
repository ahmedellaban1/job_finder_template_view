from django.contrib import admin
from .models import Company, Job, Category

admin.site.register(Job)
admin.site.register(Category)
admin.site.register(Company)
