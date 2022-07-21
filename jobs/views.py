from django.shortcuts import render, get_object_or_404, reverse
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from django.views import generic, View
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from .models import JobListing, CoverLetter, UserProfile
from .forms import (
    CoverLetterForm, AddJobListingForm, EditJobListingForm,
    EditUserProfileForm
    )


class SuperuserRequiredMixin(LoginRequiredMixin, UserPassesTestMixin):
    """
    Allows only superusers to be able to login to a page.
    requests superusers only
    """
    def test_func(self):
        return self.request.user.is_superuser


class JobListingView(generic.ListView):
    """
        Creates a list of job listings that can be viewed,
        Receives queryset from JobListing model,
        Returns 5 item page that paginates
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
        """
            displays single job listing with details
            receives a single object from the queryset, has a toggle
            that saves job to favourites,
            returns job details, saved toggle and application form
        """
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
                'cover_letter': CoverLetterForm()
            }
        )

    def post(self, request, slug, *args, **kwargs):
        """
            posts data fromt he cover letter form to the database,
            validates the form, if form is valid sends a message
            to user and returns joblisting page
        """
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
            messages.success(request, "You have succesfully applied")
            cover_letter.save()
        else:
            cover_letter_form = CoverLetterForm()
        # redirects to job_listing.html when job has been aplied for.
        return HttpResponseRedirect(reverse('job_listing'))


class AddJobListingView(
        SuperuserRequiredMixin, SuccessMessageMixin, generic.CreateView):
    """
        Allows for the creation of a new jobs listing,
        accepts only users with permissions and validates the form.
    """

    model = JobListing
    template_name = 'add_job_listing.html'
    form_class = AddJobListingForm
    success_message = "Job Has Been Sent to Drafts"

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class EditJobListingView(
        SuccessMessageMixin, SuperuserRequiredMixin, generic.UpdateView):
    """
        Allows for the editing of an existing job listing,
        passes SuperuserRequired,
        if successful shows message of success
    """

    model = JobListing
    template_name = 'edit_job_listing.html'
    queryset = JobListing.objects.all()
    form_class = EditJobListingForm
    success_message = "Job has been successfully updated"


class DeleteJobListingView(
                SuccessMessageMixin, SuperuserRequiredMixin,
                generic.DeleteView
                ):
    """
        Allows for the deletion of a jobs listing
        passes SuperuserRequired,
        if successful shows message of success,
        returns jobs listing page
    """

    model = JobListing
    template_name = 'delete_job_listing.html'
    queryset = JobListing.objects.all()
    success_url = reverse_lazy("job_listing")
    success_message = "Job has been deleted"


class JobApplicationsView(SuperuserRequiredMixin, generic.ListView):
    """
        Displays a list view of all the job applications
        passes in SuperuserRequired mixin
        returns all user based applications
    """
    model = CoverLetter
    template_name = 'job_applicants.html'
    querysetlist = CoverLetter.objects.all()


class JobApplicationDetailsView(SuperuserRequiredMixin, generic.DetailView):
    """
    Displays job details and the users application,
    passes SuperuserRequired, and primary key to link to
    only specific job application
    """

    def get(self, request, pk,  *args, **kwargs):

        queryset = CoverLetter.objects.all()
        application = get_object_or_404(queryset, pk=pk)

        joblisting = application.jobs

        return render(
            request,
            'job_application_details.html',
            {
                'job': joblisting,
                'application': application
            }
        )

# Adding job listings to favourites
# (https://www.youtube.com/watch?v=1XiJvIuvqhs&ab_channel=AbhishekVerma)


class JobSave(LoginRequiredMixin, View):
    """
        Allows for the toggling of job saves.

    """
    def post(self, request, slug):
        job = get_object_or_404(JobListing, slug=slug)

        if job.saves.filter(id=request.user.id).exists():
            messages.success(
                request, "You have removed this job from your favourites"
                )
            job.saves.remove(request.user)
        else:
            job.saves.add(request.user)
            messages.success(request, "Job saved ")
        # Redirects to current page when the user saves or removes saves job
        return HttpResponseRedirect(reverse('job_details', args=[slug]))


class JobSaveList(LoginRequiredMixin, generic.ListView):
    """
        Displays saved jobs by requesting the current user ID
        returns saved jobs page

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
        Pulls details from the UserProfile model
        returns details of a user profile
    """

    def get(self, request, pk, *args, **kwargs):
        user = get_object_or_404(User, pk=pk)
        user_details = get_object_or_404(UserProfile, user=user)

        return render(
            request,
            'user_profile.html',
            {
                'user_details': user_details,
            }
        )


class EditUserProfileView(
        SuccessMessageMixin, SuperuserRequiredMixin, generic.UpdateView):

    """
        Allows for the editing of an existing user profile
        returns home page once updated, shows success message
    """
    model = UserProfile
    queryset = UserProfile.objects.all()
    template_name = 'edit_user_profile.html'
    form_class = EditUserProfileForm
    success_url = reverse_lazy('home')
    success_message = "Profile was Updated Succesfully"


class DisplayDraftJobList(SuperuserRequiredMixin, generic.ListView):
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


class DraftJobListingDetail(SuperuserRequiredMixin, generic.DetailView):
    """
        Allows the details of a draft job listing to be viewed
    """

    def get(self, request, slug, *args, **kwargs):
        queryset = JobListing.objects.filter(composed_status=0)
        job = get_object_or_404(queryset, slug=slug)

        return render(
            request,
            'draft_details.html',
            {
                'job': job,
            }
        )

    def post(self, request, slug, *args, **kwargs):
        queryset = JobListing.objects.filter(composed_status=0)
        job = get_object_or_404(queryset, slug=slug)
        # sets composed status from draft to published, saves the action
        if job.composed_status == 0:
            job.composed_status = 1
            messages.success(
                request, "You have succesfully posted the job.")
            job.save()
        # Redirects to home page when job has been published.
        return HttpResponseRedirect(reverse('home'))
