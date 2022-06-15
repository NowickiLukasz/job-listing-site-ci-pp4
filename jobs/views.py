from django.shortcuts import render, get_object_or_404
from django.views import generic
from .models import JobListing
# from .forms import JobListingForm

# Create your views here.

class JobListingView(generic.ListView):
    model = JobListing
    queryset = JobListing.objects.filter(composed_status=1)
    template_name = 'job_listing.html'
    paginate_by = 5


class JobListingDetail(generic.DetailView):
    
    def get(self, request, slug, *args, **kwargs):
        queryset = JobListing.objects.filter(composed_status=1)
        job = get_object_or_404(queryset, slug=slug)
        saves = False
        if job.saves.filter(id=self.request.user.id).exists():
            saves = True

        return render(
            request,
            'job_details.html',
            {
                'job': job,
                'saves': saves
            }
        )

class AddJobListingView(generic.CreateView):

    model = JobListing
    queryset = JobListing.objects.all()
    template_name = 'add_job_listing.html'
    fields = [
        'title', 'employer', 'location', 'salary', 'postition_type',
        'description'
    ]