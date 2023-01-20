import pytest
from django.contrib.auth.models import User

from subscriptions.models import Subscription


@pytest.mark.django_db
def test_should_create_subscription_when_user_post_saved(self):
    user = User.objects.create(
        username="admin",
    )
    user.save()
    assert Subscription.objects.filter(user=user).exists()
