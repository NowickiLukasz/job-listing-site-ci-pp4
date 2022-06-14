from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from django_countries.fields import CountryField


STATUS = ((0, "Draft"), (1, "Published"))
POSITION_TYPE = (("Full-time", "Full-time"), ("Part-time", "Part-time"))

class JobListing(models.Model):
    title = models.CharField(max_length=150, unique=True)
    slug = models.CharField(max_length=150, unique=True)
    employer = models.ForeignKey(User, on_delete=models.CASCADE)
    location = models.CharField(max_length=300)
    salary = models.SmallIntegerField()
    postition_type = models.CharField(max_length=20, choices=POSITION_TYPE)
    description = models.TextField()
    updated_on = models.DateTimeField(auto_now=True)
    saves = models.ManyToManyField(User, related_name='saved_jobs', blank=True)
    created_on = models.DateTimeField(auto_now_add=True)
    composed_status = models.IntegerField(choices=STATUS, default=0)
    


    def __str__(self):
        return self.title


    def numbers_of_times_saved(self):
        return self.saves.count()


class CoverLetter(models.Model):
    jobs = models.ForeignKey(
        JobListing, on_delete=models.CASCADE, related_name="applications"
        )
    title = models.CharField(max_length=150, unique=True)
    location = models.CharField(max_length=300)
    postition_type = models.CharField(max_length=20, choices=POSITION_TYPE)
    salary = models.SmallIntegerField()
    cover_letter = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)


class UserProfile(models.Model):

    GENDERS = (("MALE", "MALE"), ("FEMALE", "FEMALE"), ("OTHER", "OTHER"))
    TITLE = (
        ('mr', 'mr'), ('ms', 'ms'), ('mrs', 'mrs')
    )
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="user_profile"
        )
    title = models.CharField(max_length=10, choices=TITLE)
    f_name = models.CharField(max_length=50)
    l_name = models.CharField(max_length=50)
    date_of_birth = models.DateField()
    country = CountryField()
    gender = models.CharField(max_length=15, choices=GENDERS, default="Female")

    