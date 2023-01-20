from rest_framework import serializers

from apps.api.v1.serializers import ApplicationSerializer
from subscriptions.models import Subscription


class SubscriptionSerializer(serializers.ModelSerializer):
    applications = ApplicationSerializer(many=True, read_only=True)

    class Meta:
        model = Subscription
        fields = "__all__"

    def get_application(self, obj):
        return obj.application.name


class UserSubscriptionSerializer(serializers.ModelSerializer):
    application = ApplicationSerializer(many=True, read_only=True)
    plan = serializers.SerializerMethodField()

    class Meta:
        model = Subscription
        fields = ["plan", "application", "active"]

    def get_plan(self, obj):
        return f"{obj.plan.name} - {obj.plan.price}$"
