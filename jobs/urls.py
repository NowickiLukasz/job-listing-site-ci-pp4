from django.urls import path
from .views import (
    JobListingView, JobListingDetail, AddJobListingView, EditJobListingView,
    DeleteJobListingView, JobApplicationsView
)

urlpatterns = [
    path('home/', JobListingView.as_view(), name='home'),
    path('job-listing/', JobListingView.as_view(), name='job_listing'),
    path('add-job/', AddJobListingView.as_view(), name='add_job'),
    path('edit-job/<int:pk>', EditJobListingView.as_view(), name='edit_job'),
    path('delete-job/<int:pk>', DeleteJobListingView.as_view(), name='delete_job'),
    path('job-applicants/', JobApplicationsView.as_view(), name='job_applicants'),
    path('<slug:slug>/', JobListingDetail.as_view(), name='job_details'),
  

]