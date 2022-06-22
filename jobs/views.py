from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic, View
from django.http import HttpResponseRedirect
from .models import JobListing, CoverLetter
from django.urls import reverse_lazy
from .forms import(
    CoverLetterForm, AddJobListingForm, EditJobListingForm
    ) 

# Create your views here.

class JobListingView(generic.ListView):
    """
    Creates a list of job listings that can be viewed
    """
    model = JobListing
    queryset = JobListing.objects.filter(composed_status=1)
    template_name = 'job_listing.html'
    paginate_by = 5


class JobListingDetail(generic.DetailView):
    """
        Allows the details of a job listing to be viewed
    """
    
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
                'saves': saves,
                # 'submited': False,
                'cover_letter': CoverLetterForm()
            }
        )
    
    def post(self, request, slug, *args, **kwargs):
        queryset = JobListing.objects.filter(composed_status=1)
        job = get_object_or_404(queryset, slug=slug)
        saves = False
        if job.saves.filter(id=self.request.user.id).exists():
            saves = True

        cover_letter_form = CoverLetterForm(data=request.POST)
        
        if cover_letter_form.is_valid():
            cover_letter_form.instance.full_name = request.user.username
            cover_letter = cover_letter_form.save(commit=False)
            cover_letter.job = job
            cover_letter.save()
        else:
            cover_letter_form = CoverLetterForm()
        
        return render(
            request,
            'job_details.html',
            {
                'job': job,
                'saves': saves,
                # 'submited': True,
                'cover_letter': CoverLetterForm()
            }
        )


class AddJobListingView(generic.CreateView):
    """
        Allows for the creation of a new jobs listing
    """

    model = JobListing
    queryset = JobListing.objects.all()
    template_name = 'add_job_listing.html'
    form_class = AddJobListingForm
    # fields = [
    #     'title', 'employer', 'location', 'salary', 'postition_type',
    #     'description'
    # ]

    


class EditJobListingView(generic.UpdateView):
    """
        Allows for the editing of an existing job listing
    """

    model = JobListing
    template_name = 'edit_job_listing.html'
    queryset = JobListing.objects.all()
    form_class = EditJobListingForm
    # fields = [
    #     'title', 'employer', 'location', 'salary', 'postition_type',
    #     'description'
    # ]


class DeleteJobListingView(generic.DeleteView):
    """
        Allows for the deletion of a jobs listing
    """

    model = JobListing
    template_name = 'delete_job_listing.html'
    queryset = JobListing.objects.all()
    success_url = reverse_lazy("job_listing")


class JobApplicationsView(generic.ListView):
    """
        Displays a list view of all the job applications
    """

    model = CoverLetter
    template_name = 'job_applicants.html'
    querysetlist = CoverLetter.objects.all()


