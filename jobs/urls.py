from django.urls import path
from .views import JobListingView, JobListingDetail, AddJobListingView

urlpatterns = [
    path('home/', JobListingView.as_view(), name='home'),
    path('job-listing/', JobListingView.as_view(), name='job_listing'),
    path('add-job/', AddJobListingView.as_view(), name='add_job'),
    path('<slug:slug>/', JobListingDetail.as_view(), name='job_details'),
    

]