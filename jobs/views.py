from django.shortcuts import render, get_object_or_404, reverse
from django.contrib.auth.mixins import LoginRequiredMixin
 
from django.views import generic, View
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from .models import JobListing, CoverLetter, UserProfile
from .forms import (
    CoverLetterForm, AddJobListingForm, EditJobListingForm,
    EditUserProfileForm
    )


class JobListingView(generic.ListView):
    """
    Creates a list of job listings that can be viewed
    """
    model = JobListing
    queryset = JobListing.objects.filter(composed_status=1)
    template_name = 'job_listing.html'
    paginate_by = 5


class JobListingDetail(LoginRequiredMixin, generic.DetailView):
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
            # sets full name instance to username
            cover_letter_form.instance.full_name = request.user.username
            cover_letter = cover_letter_form.save(commit=False)
            cover_letter.user = request.user
            cover_letter.jobs = job
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


class AddJobListingView(LoginRequiredMixin, generic.CreateView):
    """
        Allows for the creation of a new jobs listing
    """

    model = JobListing
    template_name = 'add_job_listing.html'
    form_class = AddJobListingForm

   
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
    

class EditJobListingView(LoginRequiredMixin, generic.UpdateView):
    """
        Allows for the editing of an existing job listing
    """

    model = JobListing
    template_name = 'edit_job_listing.html'
    queryset = JobListing.objects.all()
    form_class = EditJobListingForm


class DeleteJobListingView(LoginRequiredMixin, generic.DeleteView):
    """
        Allows for the deletion of a jobs listing
    """

    model = JobListing
    template_name = 'delete_job_listing.html'
    queryset = JobListing.objects.all()
    success_url = reverse_lazy("job_listing")


class JobApplicationsView(LoginRequiredMixin, generic.ListView):
    """
        Displays a list view of all the job applications
    """

    model = CoverLetter
    template_name = 'job_applicants.html'
    querysetlist = CoverLetter.objects.all()


class JobApplicationDetailsView(LoginRequiredMixin, generic.DetailView):

    def get(self, request, pk,  *args, **kwargs):
        queryset = CoverLetter.objects.all()
        application = get_object_or_404(queryset, pk=pk)

        joblisting = application.jobs

        return render(
            request,
            'job_application_details.html',
            {
                'job': joblisting,
                # 'submited': False,
                'application': application
            }
        )


class JobSave(LoginRequiredMixin, View):
    """
        Allows for the toggling of job saves.

    """
    def post(self, request, slug):
        job = get_object_or_404(JobListing, slug=slug)

        if job.saves.filter(id=request.user.id).exists():
            job.saves.remove(request.user)
        else:
            job.saves.add(request.user)
        
        return HttpResponseRedirect(reverse('job_details', args=[slug]))


class JobSaveList(LoginRequiredMixin, generic.ListView):
    """
        Displays saved jobs 

    """
    def get(self, request):
        saved_jobs = JobListing.objects.filter(saves=self.request.user)
        
        return render(
            request,
            'saved_jobs.html',
            {
                'saved_jobs': saved_jobs
            }
        )


class UserProfilePage(View):
    """
        Pulls details from the UserProfile model so that user details
         can be rendered on the site
    """

    def get(self, request, pk, *args, **kwargs):
        # user_details = UserProfile.objects.all()
        user = get_object_or_404(User, pk=pk)
        user_details = get_object_or_404(UserProfile, user=user)
        
        return render(
            request,
            'user_profile.html',
            {
                'user_details': user_details,
                # 'user_profile': user_profile,
            }
        )


class EditUserProfileView(LoginRequiredMixin, generic.UpdateView):

    """
        Allows for the editing of an existing user profile
    """
    model = UserProfile
    queryset = UserProfile.objects.all()
    template_name = 'edit_user_profile.html'
    form_class = EditUserProfileForm
    success_url = reverse_lazy('home')


class DisplayDraftJobList(LoginRequiredMixin, generic.ListView):
    """
        Allows the Admin User to display job listings that are not published 
        yet
    """
    def get(self, request):
        drafts = JobListing.objects.filter(composed_status=0)
        
        return render(
            request,
            'drafts.html',
            {
                'drafts': drafts,
            }
        )


class DraftJobListingDetail(LoginRequiredMixin, generic.DetailView):
    """
        Allows the details of a job listing to be viewed
    """
    
    def get(self, request, slug, *args, **kwargs):
        if request.user.is_superuser:
            queryset = JobListing.objects.filter(composed_status=0)
            job = get_object_or_404(queryset, slug=slug)

            return render(
                request,
                'draft_details.html',
                {
                    'job': job,
                }
            )
        else:
            return HttpResponseRedirect(reverse('home'))

    # def post(self, request, slug, *args, **kwargs):
    #     queryset = JobListing.objects.filter(composed_status=0)
    #     job = get_object_or_404(queryset, slug=slug)