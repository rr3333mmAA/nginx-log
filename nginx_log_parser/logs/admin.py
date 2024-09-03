from django.contrib import admin
from .models import NginxLogEntry


@admin.register(NginxLogEntry)
class NginxLogEntryAdmin(admin.ModelAdmin):
    list_display = ('remote_ip', 'time', 'request', 'response', 'bytes')
    search_fields = ('remote_ip', 'request')
    list_filter = ('request', 'response', 'time')
