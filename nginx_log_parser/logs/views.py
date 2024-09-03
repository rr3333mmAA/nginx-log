from rest_framework import viewsets, filters
from .models import NginxLogEntry
from .serializers import NginxLogEntrySerializer


class NginxLogEntryViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Nginx log entries to be viewed or edited.
    """

    queryset = NginxLogEntry.objects.all()
    serializer_class = NginxLogEntrySerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['ip_address', 'uri']
    ordering_fields = ['timestamp', 'status_code']