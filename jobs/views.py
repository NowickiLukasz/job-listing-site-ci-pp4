from django.shortcuts import render, get_object_or_404
from django.views import generic
from .models import JobListing, CoverLetter
from django.urls import reverse_lazy
from .forms import CoverLetterForm

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


class EditJobListingView(generic.UpdateView):

    model = JobListing
    template_name = 'edit_job_listing.html'
    queryset = JobListing.objects.all()
    fields = [
        'title', 'employer', 'location', 'salary', 'postition_type',
        'description'
    ]


class DeleteJobListingView(generic.DeleteView):

    model = JobListing
    template_name = 'delete_job_listing.html'
    queryset = JobListing.objects.all()
    success_url = reverse_lazy("job_listing")


class JobApplicationsView(generic.ListView):

    model = CoverLetter
    template_name = 'job_applicants.html'
    querysetlist = CoverLetter.objects.all()
    