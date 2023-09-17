from django.core.management.base import BaseCommand
from apps.rates.services import get_rates


class Command(BaseCommand):
    help = 'Make a position drug ordering in admin-panel for every Rate. Need only when rate view_position is zero'

    def handle(self, *args, **options):
        for rate in get_rates():
            rate.save()
        
        self.stdout.write(self.style.SUCCESS('All rates successfully updated'))