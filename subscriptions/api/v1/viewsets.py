from rest_framework import authentication
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from subscriptions.models import Subscription
from .serializers import SubscriptionSerializer, UserSubscriptionSerializer
from rest_framework import viewsets
from rest_framework.status import HTTP_200_OK


class SubscriptionViewSet(viewsets.ViewSet):
    serializer_class = SubscriptionSerializer
    authentication_classes = (authentication.SessionAuthentication, authentication.TokenAuthentication)
    permission_classes = (IsAuthenticated,)
    queryset = Subscription.objects.all()

    def retrieve(self, request, *args, pk=None):
        queryset = get_object_or_404(Subscription, pk=pk)
        serializer = self.serializer_class(queryset)
        return Response(serializer.data, status=HTTP_200_OK)

    def list(self, request):
        serializer = UserSubscriptionSerializer(self.queryset, many=True)
        return Response(serializer.data)

    def destroy(self, request, pk=None):
        queryset = get_object_or_404(Subscription, pk=pk)
        if queryset.active:
            queryset.active = False
            queryset.save
        return Response(status=HTTP_200_OK)

    def get_object(self):
        pk = self.kwargs.get('pk')
        obj = get_object_or_404(self.queryset, pk=pk)
        return obj

    def partial_update(self, request, *args, **kwargs):
        partial = kwargs['partial'] = True
        instance = self.get_object()
        serializer = self.serializer_class(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
