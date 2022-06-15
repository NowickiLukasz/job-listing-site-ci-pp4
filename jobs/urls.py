from django.urls import path
from .views import JobListingView

urlpatterns = [
    path('joblisting/', JobListingView.as_view(), name='joblisting')
]