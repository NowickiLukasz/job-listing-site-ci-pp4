from .models import UserProfile


def get_profile(request):

    if request.user.is_authenticated:
        profile = UserProfile.objects.get(user=request.user)
    else:
        profile = None

    context = {
        'profile': profile
    }

    return context
