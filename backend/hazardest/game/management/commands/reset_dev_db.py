from django.core.management import call_command
from django.core.management.base import BaseCommand
from django.contrib.auth.models import User

from ...tests.fixtures import create_game_with_players
from ...utils.create_cards import create_cards


class Command(BaseCommand):
    help = 'resets the dev DB'

    def handle(self, **options):
        call_command('flush')

        # create admin user
        User.objects.create_superuser(username='admin',
                                      email='jordan.slaman@gmail.com',
                                      password='admin')

        create_cards()
        create_game_with_players()
