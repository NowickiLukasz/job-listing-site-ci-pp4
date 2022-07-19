from django.contrib.auth.models import User
from .models import UserProfile


def get_profile(request):
    """
        Creates a profile context that can be used throught the app
    """

    if request.user.is_authenticated:
        # user = User.objects.get(username=request.user)
        profile = UserProfile.objects.get(user=request.user)
    else:
        profile = None

    context = {
        # 'user': user,
        'profile': profile,

    }

    return context
