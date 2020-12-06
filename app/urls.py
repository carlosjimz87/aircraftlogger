from django.urls import include, path
from rest_framework import routers
from app.views import FlightViewSet, AircraftViewSet

router = routers.DefaultRouter()
router.register(r'aircraft', AircraftViewSet)
router.register(r'flight', FlightViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
