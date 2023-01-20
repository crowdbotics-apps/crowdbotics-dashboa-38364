from rest_framework import authentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from apps.models import Applications
from .serializers import ApplicationSerializer
from rest_framework import viewsets
from rest_framework.status import HTTP_201_CREATED
from rest_framework.authtoken.models import Token

from .utils import generate_random_app_name, handle_related_subscription


class ApplicationViewSet(viewsets.GenericViewSet):
    serializer_class = ApplicationSerializer
    authentication_classes = (authentication.TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    queryset = Applications.objects.all()

    def get_serializer(self, *args, **kwargs):
        return self.serializer_class(*args, **kwargs)

    def create(self, request, *args, **kwargs):
        request_token = Token.objects.filter(key=request.auth).first()
        subscription = request_token.user.subscription_user
        generate_random_app_name(request)
        app = handle_related_subscription(request, subscription)
        serializer = self.get_serializer(app)
        return Response(serializer.data, status=HTTP_201_CREATED)


