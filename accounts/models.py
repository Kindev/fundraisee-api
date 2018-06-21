from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from rest_framework.authtoken.models import Token
from django.dispatch import receiver


class UserProfile(models.Model):
    # We build on top of default django user model
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name='profile'
    )
    # additional fields we want to store for user.
    avatar = models.URLField(default='', blank=True)

    def __str__(self):
        return self.user.username


# automatically create a token for each new user
@receiver(post_save, sender=User)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)


# New superuser profile
@receiver(post_save, sender=User)
def create_superuser_profile(sender, instance, created, **kwargs):
    if created and instance.is_superuser:
        UserProfile.objects.create(
            user=instance,
            avatar='https://api.adorable.io/avatar/200/admin'
        )