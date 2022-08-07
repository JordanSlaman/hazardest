import hashlib

from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# from allauth.account.signals import user_signed_up


class Profile(models.Model):

    def __str__(self):
        return f'Profile for {self.user}'

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    gravatar_url = models.CharField(max_length=100, default=None)

    wins = models.IntegerField(default=0)
    losses = models.IntegerField(default=0)

    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            email = instance.email.lower().encode('utf-8')
            gravatar_url = "https://www.gravatar.com/avatar/" + hashlib.md5(email).hexdigest() + "?d=identicon&pg"
            Profile.objects.create(user=instance, gravatar_url=gravatar_url)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.profile.save()


# allauth.account.signals.email_added(request, user, email_address)