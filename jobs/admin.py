from django.contrib import admin
from .models import JobListing
from django_summernote.admin import SummernoteModelAdmin

# Register your models here.

@admin.register(JobListing)
class JobAdmin(SummernoteModelAdmin):
    summernote_fields = ('description')
