import datetime
from django.utils import timezone

from django.core.management.base import BaseCommand, CommandError
from django.conf import settings

from content.models import DownloadLink





class Command(BaseCommand):
    def handle(self, *args, **options):
        print 'manage py command'
        timezone.activate(settings.TIME_ZONE)
        maxage = datetime.timedelta(minutes=2)
        now = timezone.now()
        print now
        for link in DownloadLink.objects.all():
            if (now - link.since) > maxage:
                print link.since
                link.delete()