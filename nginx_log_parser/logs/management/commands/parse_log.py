import json
import requests
import re

from datetime import datetime
from django.core.management.base import BaseCommand

from logs.models import NginxLogEntry


class Command(BaseCommand):
    help = 'Parses a JSON log file and stores the data in the database.'

    def add_arguments(self, parser):
        parser.add_argument('log_url', type=str, help='URL to the Google Drive txt JSON-like log file.')

    def handle(self, *args, **options):
        log_url = options['log_url']


        # Check if the URL is a valid Google Drive URL
        if not re.match(r'https://drive.google.com/file/d/.*', log_url):
            self.stdout.write(self.style.ERROR('Invalid Google Drive URL. URL should be in the format: "https://drive.google.com/file/d/FILE_ID/view"'))
            return

        # Extract the file ID from the URL and download the file
        file_id = log_url.split('/')[5]
        response = requests.get(f'https://drive.google.com/uc?export=download&id={file_id}')

        # Save the log entries to the database
        for line in response.text.split('\n'):
            if not line:
                continue

            log_data = json.loads(line)

            log_entry = NginxLogEntry(
                time=datetime.strptime(log_data['time'], '%d/%b/%Y:%H:%M:%S %z'),
                remote_ip=log_data['remote_ip'],
                remote_user=log_data['remote_user'],
                request=log_data['request'],
                response=log_data['response'],
                bytes=log_data['bytes'],
                referrer=log_data['referrer'],
                agent=log_data['agent']
            )
            log_entry.save()

        self.stdout.write(self.style.SUCCESS('Log file processed successfully.'))
