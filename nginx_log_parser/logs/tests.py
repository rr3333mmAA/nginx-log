from datetime import datetime

from django.test import TestCase
from logs.models import NginxLogEntry


class NginxLogEntryTestCase(TestCase):
    def setUp(self):
        NginxLogEntry.objects.create(
            time=datetime.strptime('17/May/2015:08:05:32 +0000', '%d/%b/%Y:%H:%M:%S %z'),
            remote_ip='93.180.71.3',
            remote_user='-',
            request='GET /downloads/product_1 HTTP/1.1',
            response=304,
            bytes=0,
            referrer='-',
            agent='Debian APT-HTTP/1.3 (0.8.16~exp12ubuntu10.21)'
        )

    def test_log_entry_creation(self):
        log_entry = NginxLogEntry.objects.get(remote_ip='93.180.71.3')
        self.assertEqual(log_entry.response, 304)
