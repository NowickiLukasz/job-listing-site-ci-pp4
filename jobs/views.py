from django.shortcuts import render
from django.views import generic
from .models import JobListing

# Create your views here.

class JobListingView(generic.ListView):
    model = JobListing
    queryset = JobListing.objects.filter(composed_status=1)
    template_name = 'job_listing.html'
    paginate_by = 10