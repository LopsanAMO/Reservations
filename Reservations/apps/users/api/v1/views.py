import json
from django.shortcuts import HttpResponse
from django.http import Http404
from rest_framework import viewsets, mixins
from rest_framework.permissions import AllowAny
from Reservations.apps.users.models import User
from Reservations.apps.users.permissions import IsUserOrReadOnly
from Reservations.apps.users.api.v1.serializers import CreateUserSerializer, UserSerializer


class UserViewSet(mixins.RetrieveModelMixin,
                  mixins.UpdateModelMixin,
                  viewsets.GenericViewSet):
    """
    Updates and retrieves user accounts
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsUserOrReadOnly,)

    def get_object(self):
        try:
            return User.objects.get(id=self.request.user.id)
        except Exception:
            raise Http404

    def get(self, request):
        return self.retrieve(request)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)


class UserCreateViewSet(mixins.CreateModelMixin,
                        viewsets.GenericViewSet):
    """
    Creates user accounts
    """
    queryset = User.objects.all()
    serializer_class = CreateUserSerializer
    permission_classes = (AllowAny,)
