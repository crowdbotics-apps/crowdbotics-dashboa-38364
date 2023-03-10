
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .viewsets import UserViewSet
router = DefaultRouter()
router.register('user/subscriptions', UserViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
