from django.contrib import admin
from .models import Company, Job, Category


class JobAdmin(admin.ModelAdmin):
    list_display = ('title', 'company', 'job_type', 'category')
    search_fields = ('title', 'description')
    list_filter = ('category', 'vacancy', 'experience')


class CategoryAdmin(admin.ModelAdmin):
    search_fields = ('name',)


class CompanyAdmin(admin.ModelAdmin):
    list_display = ('name', 'website', 'email')
    search_fields = ('name', 'website', 'email')


admin.site.register(Job, JobAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Company, CompanyAdmin)
