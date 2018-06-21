from django.contrib.auth.models import User

from accounts.models import UserProfile


def create_user(*args, **kwargs):
    new_user = User.objects.create_user(*args, **kwargs)
    UserProfile.objects.create(user=new_user)
    return new_user
