from django.urls import include, path
from rest_framework import routers
from app.views import FlightViewSet, AircraftViewSet, AirportViewSet, ReportViewSet

router = routers.DefaultRouter()
router.register(r'aircrafts', AircraftViewSet)
router.register(r'flights', FlightViewSet)
router.register(r'airports', AirportViewSet)
router.register(r'report', ReportViewSet, basename='report')

urlpatterns = [
    # path('report/', ReportView.as_view(), name='report-list'),
    path('', include(router.urls)),
]
