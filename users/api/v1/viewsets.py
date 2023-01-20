from rest_framework import authentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.status import HTTP_200_OK
from rest_framework.response import Response

from apps.models import Applications
from apps.api.v1.serializers import ApplicationSerializer
from subscriptions.models import Subscription
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
        token = Token.objects.get(key=request.auth)
        subscription = Subscription.objects.get(user_id=token.user.id)
        apps = Applications.objects.filter(subscription=subscription)
        #serializer = ApplicationSerializer(Applications.objects.prefetch_related('subscription'), many=True)
        serializer = ApplicationSerializer(apps, many=True)

        data = {
            "id":subscription.id,
            "owner": subscription.user.username,
            "active": subscription.active,
            "plan_name": subscription.plan.name,
            "plan_description": subscription.plan.description,
            "plan_price": subscription.plan.price,
            "applications": serializer.data
        }

        return Response(data, status=HTTP_200_OK)
