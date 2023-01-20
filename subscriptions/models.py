from plans.models import Plan
from users.models import User
from apps.models import Applications
from django.db import models


class Subscription(models.Model):
    user = models.OneToOneField(User, on_delete=models.DO_NOTHING, related_name="subscription_user")
    application = models.ForeignKey(Applications, on_delete=models.SET_NULL, related_name="subscription_app", null=True)
    plan = models.ForeignKey(Plan, on_delete=models.SET_NULL, related_name="subscription_plan", null=True)
    active = models.BooleanField("Active", default=True)
    created_at = models.DateTimeField("Created at", auto_now_add=True)
    update_at = models.DateTimeField("Update at", auto_now_add=True)
