from rest_framework import authentication
from rest_framework.permissions import IsAuthenticated
from subscriptions.models import Subscription
from .serializers import SubscriptionSerializer
from rest_framework import viewsets


class SubscriptionViewSet(viewsets.ViewSet):
    serializer_class = SubscriptionSerializer
    authentication_classes = (authentication.SessionAuthentication, authentication.TokenAuthentication)
    permission_classes = (IsAuthenticated,)
    queryset = Subscription.objects.all()

    def retrieve(self, request, *args, pk=None):
        pass

    def list(self, request):
        pass

    def destroy(self, request, pk=None):
        pass

    def partial_update(self, request, pk=None):
        pass