from django.core.management.base import BaseCommand

from ...utils.create_cards import create_cards


class Command(BaseCommand):
    help = 'Creates a deck of cards once.'

    def handle(self, **options):
        create_cards()
