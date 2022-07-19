from django.db.models.signals import post_save
from django.contrib.auth.models import User
from .models import UserProfile

# Auto creating user profile with signals
# (https://ordinarycoders.com/django-custom-user-profile)


def create_profile(sender, instance, created, **kwargs):
    """
        Automaticaly creates a profile once user is created from registration
    """
    if created:
        UserProfile.objects.create(
            user=instance,

        )


post_save.connect(create_profile, sender=User)
