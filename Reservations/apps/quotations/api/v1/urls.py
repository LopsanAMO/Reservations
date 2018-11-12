from django.urls.conf import path, include
from rest_framework.routers import DefaultRouter
from Reservations.apps.quotations.api.v1.views import CreateReservationViewSet, ReservationViewSet


router = DefaultRouter()
router.register(r'', CreateReservationViewSet)
router.register(r'reservation', ReservationViewSet)

urlpatterns = [
    path('', include(router.urls))
]