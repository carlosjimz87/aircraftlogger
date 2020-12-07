from django.urls import include, path
from rest_framework import routers
from app.views import FlightViewSet, AircraftViewSet, AirportViewSet

router = routers.DefaultRouter()
router.register(r'aircrafts', AircraftViewSet)
router.register(r'flights', FlightViewSet)
router.register(r'airports', AirportViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
