from django.db import models


class NginxLogEntry(models.Model):
    time = models.DateTimeField()
    remote_ip = models.GenericIPAddressField()
    remote_user = models.CharField(max_length=50)
    request = models.CharField(max_length=50)
    response = models.IntegerField()
    bytes = models.IntegerField()
    referrer = models.CharField(max_length=2048)
    agent = models.CharField(max_length=2048)

    def __str__(self):
        return f"{self.remote_ip} - {self.request} - {self.response}"
