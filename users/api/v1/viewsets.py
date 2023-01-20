from rest_framework import authentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.status import HTTP_200_OK
from rest_framework.response import Response

from subscriptions.api.v1.serializers import UserSubscriptionSerializer
from users.models import User
from .serializers import UserSerializer
from rest_framework import viewsets
from rest_framework.authtoken.models import Token


class UserViewSet(viewsets.GenericViewSet):
    serializer_class = UserSerializer
    authentication_classes = (authentication.TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    queryset = User.objects.all()

    def list(self, request):
        request_token = Token.objects.filter(key=request.auth).first()
        queryset = request_token.user.subscription_user
        serializer = UserSubscriptionSerializer(queryset)
        return Response(serializer.data, status=HTTP_200_OK)
