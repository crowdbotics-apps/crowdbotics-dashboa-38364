from rest_framework import authentication
from rest_framework.permissions import IsAuthenticated

from apps.models import Applications
from .serializers import ApplicationSerializer
from rest_framework import viewsets

class ApplicationViewSet(viewsets.ViewSet):
    serializer_class = ApplicationSerializer
    authentication_classes = (authentication.SessionAuthentication, authentication.TokenAuthentication)
    permission_classes = (IsAuthenticated,)
    queryset = Applications.objects.all()

    def retrieve(self, request, *args, pk=None):
        pass
