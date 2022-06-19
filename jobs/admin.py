from django.contrib import admin
from .models import JobListing, CoverLetter
from django_summernote.admin import SummernoteModelAdmin

# Register your models here.

@admin.register(JobListing)
class JobAdmin(SummernoteModelAdmin):
    
    list_display = (
        'title', 'slug', 'composed_status', 'created_on', 
        'postition_type',
        )
    list_filter = ('composed_status', 'created_on', 'postition_type')
    search_fields = ['title', 'description']
    prepopulated_fields = {'slug': ('title',)}
    summernote_fields = ('description')
    actions = ['approve_joblisting']

    def approve_joblisting(self, request, queryset):
        queryset.update(approved=True)


@admin.register(CoverLetter)
class CoverLetterAdmin(SummernoteModelAdmin):

    list_display = ('full_name', 'jobs', 'title', 'location', 'created_on')
    list_filter = ('created_on', 'postition_type')
    summernote_fields = ('cover_letter')
    
    
