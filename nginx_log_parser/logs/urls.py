from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import NginxLogEntryViewSet

router = DefaultRouter()
router.register(r'logs', NginxLogEntryViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
]