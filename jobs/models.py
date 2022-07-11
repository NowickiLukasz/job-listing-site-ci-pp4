from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.conf import settings
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from django_countries.fields import CountryField
from django.urls import reverse


STATUS = ((0, "Draft"), (1, "Published"))
POSITION_TYPE = (("Full-time", "Full-time"), ("Part-time", "Part-time"))


class JobListing(models.Model):
    """
        Creates a model job details of job listings
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=150, unique=True)
    slug = models.CharField(max_length=150)
    location = models.CharField(max_length=300)
    salary = models.SmallIntegerField()
    postition_type = models.CharField(max_length=20, choices=POSITION_TYPE)
    description = models.TextField()
    updated_on = models.DateTimeField(auto_now=True)
    saves = models.ManyToManyField(User, related_name='saved_jobs', blank=True)
    created_on = models.DateTimeField(auto_now_add=True)
    composed_status = models.IntegerField(choices=STATUS, default=0)
    
    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title

    def numbers_of_times_saved(self):
        return self.saves.count()

    def get_absolute_url(self):
        return reverse('job_listing')


class CoverLetter(models.Model):
    """
        Creates a model for details of a cover letter
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    jobs = models.ForeignKey(
        JobListing, on_delete=models.CASCADE, related_name="applications"
        )
    full_name = models.CharField(max_length=150, default='Full Name')
    title = models.CharField(max_length=150)
    location = models.CharField(max_length=300)
    postition_type = models.CharField(max_length=20, choices=POSITION_TYPE)
    cover_letter = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title


class UserProfile(models.Model):
    """
        Creates a models for details for a user profile page
    """

    GENDERS = (("MALE", "MALE"), ("FEMALE", "FEMALE"), ("OTHER", "OTHER"))
    TITLE = (
        ('mr', 'mr'), ('ms', 'ms'), ('mrs', 'mrs')
    )
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name="user_profile"
        )
    title = models.CharField(max_length=10, choices=TITLE)
    date_of_birth = models.DateField(null=True)
    country = CountryField()
    gender = models.CharField(max_length=15, choices=GENDERS, default="Female")
    bio = models.TextField(default='Please enter a bio')

