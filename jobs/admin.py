from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import JobListing, CoverLetter, UserProfile

# Register your models here.


@admin.register(JobListing)
class JobAdmin(SummernoteModelAdmin):
    """
        Admin panel filters and fields allowing the 
        creation of job listings.
    """

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
        """
            Allows for the toggling of published or draft jobs listings
        """
        queryset.update(composed_status=True)


@admin.register(CoverLetter)
class CoverLetterAdmin(SummernoteModelAdmin):
    """
        Admin panel for job applications, 
        allows to filter date created and position status.
    """
    list_display = ('full_name', 'jobs', 'created_on')
    list_filter = ('created_on', 'postition_type')
    summernote_fields = ('cover_letter')


@admin.register(UserProfile)
class UserProfileAdmin(SummernoteModelAdmin):
    """
        Admin panel for user profiles.
    """
    list_display = ('user', 'country', 'date_of_birth')
    list_filter = ('gender', 'country', 'date_of_birth')
