from rest_framework import serializers
from subscriptions.models import Subscription


class SubscriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subscription
        fields = "__all__"


class UserSubscriptionSerializer(serializers.ModelSerializer):
    application = serializers.SerializerMethodField()
    plan = serializers.SerializerMethodField()

    class Meta:
        model = Subscription
        fields = ["plan", "application", "active"]

    def get_application(self, obj):
        return obj.application.name

    def get_plan(self, obj):
        return f"{obj.plan.name} - {obj.plan.price}$"