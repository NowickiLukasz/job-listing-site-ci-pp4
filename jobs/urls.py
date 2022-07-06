from django.urls import path
from .views import (
    JobListingView, JobListingDetail, AddJobListingView, EditJobListingView,
    DeleteJobListingView, JobApplicationsView, JobApplicationDetailsView,
    JobSave, UserProfilePage, EditUserProfileView

)

urlpatterns = [
    # homepage 
    path('', JobListingView.as_view(), name='home'),
    # joblisting page
    path('job-listing/', JobListingView.as_view(), name='job_listing'),
    # Addjob page
    path('add-job/', AddJobListingView.as_view(), name='add_job'),
    path('edit-job/<int:pk>', EditJobListingView.as_view(), name='edit_job'),
    path(
        'delete-job/<int:pk>',
        DeleteJobListingView.as_view(),
        name='delete_job'
        ),
    path(
        'job-applicants/',
        JobApplicationsView.as_view(),
        name='job_applicants'
        ),
    path(
        'job-application-details/<int:pk>',
        JobApplicationDetailsView.as_view(),
        name='application_details'
        ),
    path(
        'profile/', UserProfilePage.as_view(),
        name='user_profile'
        ),
    path(
        'edit-profile/<int:pk>/', EditUserProfileView.as_view(),
        name='edit_user_profile'
        ),
    path(
        'saved-jobs/', JobSave.as_view(), name='saved_job_listing'
    ),
    path('<slug:slug>/', JobListingDetail.as_view(), name='job_details'),
    path('saved/<slug:slug>', JobSave.as_view(), name='job_save'),
]
