from django.db.models.signals import post_save
from django.dispatch import receiver

from crowdbotics_dashboa_38364 import settings
from plans.models import Plan
from subscriptions.models import Subscription


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_client_profile(sender, instance, created, **kwargs):
    if created:
        Subscription.objects.create(user=instance)
