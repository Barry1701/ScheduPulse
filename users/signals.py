from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Profile

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    # This function is triggered whenever a new User instance is created.
    # It ensures that a corresponding Profile is created for the new user.
    if created:
        Profile.objects.get_or_create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    # This function is triggered whenever a User instance is saved.
    # It ensures that any changes to the User instance are also saved to the associated Profile.
    instance.profile.save()
