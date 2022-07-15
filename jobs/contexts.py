from .models import UserProfile
from django.contrib.auth.models import User


def get_profile(request):

    if request.user.is_authenticated:
        user = User.objects.get(username=request.user)
        profile = UserProfile.objects.get(user=request.user)
    else:
        profile = None

    context = {
        'profile': profile,
        'user': user
    }

    return context
