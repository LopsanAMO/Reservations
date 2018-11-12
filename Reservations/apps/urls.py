from django.urls.conf import path, include
from Reservations.apps.users.api.v1 import urls as APiV1UserUrls
from Reservations.apps.hotels.api.v1 import urls as APIV1HotelUrls
from Reservations.apps.quotations.api.v1 import urls as APIV1ReservationURls

urlpatterns = [
    path('v1/users/', include(APiV1UserUrls)),
    path('v1/hotels/', include(APIV1HotelUrls)),
    path('v1/reservations/', include(APIV1ReservationURls))
]