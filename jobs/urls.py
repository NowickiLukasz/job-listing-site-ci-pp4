from django.urls import path
from .views import (
    JobListingView, JobListingDetail, AddJobListingView, EditJobListingView,
    DeleteJobListingView, JobApplicationsView, JobApplicationDetailsView,
    JobSave, UserProfilePage, EditUserProfileView, JobSaveList,
    DisplayDraftJob
)

urlpatterns = [
    # homepage
    path('', JobListingView.as_view(), name='home'),
    # joblisting page
    path('job-listing/', JobListingView.as_view(), name='job_listing'),
    # Addjob page
    path('add-job/', AddJobListingView.as_view(), name='add_job'),
    # Edit Job Listing
    path('edit-job/<int:pk>', EditJobListingView.as_view(), name='edit_job'),
    # Delete JOb Listing
    path(
        'delete-job/<int:pk>',
        DeleteJobListingView.as_view(),
        name='delete_job'
        ),
    # Displays job applications
    path(
        'job-applicants/',
        JobApplicationsView.as_view(),
        name='job_applicants'
        ),
    # Displays detailed view of job applications wit cover letter
    path(
        'job-application-details/<int:pk>',
        JobApplicationDetailsView.as_view(),
        name='application_details'
        ),
    # Diaplays user profile details
    path(
        'profile/', UserProfilePage.as_view(),
        name='user_profile'
        ),
    # Allows to edit profile details
    path(
        'edit-profile/<int:pk>/', EditUserProfileView.as_view(),
        name='edit_user_profile'
        ),
    # Displays liked/saved jobs
    path(
        'saved-jobs/', JobSaveList.as_view(), name='saved_job_listing'
    ),
    # Displays jobs that have not bee published yet
    path(
        'drafts/', DisplayDraftJob.as_view(), name='drafts'
    ),
    # Displays published job listings
    path('<slug:slug>/', JobListingDetail.as_view(), name='job_details'),
    # Toggling of saved jobs
    path('saved/<slug:slug>', JobSave.as_view(), name='job_save'),
]
