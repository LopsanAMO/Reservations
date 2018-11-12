from django.urls.conf import path, include
from rest_framework.routers import DefaultRouter
from Reservations.apps.users.api.v1.views import UserViewSet, UserCreateViewSet


router = DefaultRouter()
router.register(r'', UserViewSet)
router.register(r'user', UserCreateViewSet)


urlpatterns = [
    path('', include(router.urls))
]