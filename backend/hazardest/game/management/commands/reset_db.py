from django.core.management import call_command
from django.core.management.base import BaseCommand
from django.contrib.auth.models import User

from ...tests.fixtures import create_game_with_players, create_open_game_with_players
from ...utils.create_cards import create_cards
from ...utils.env import env_config


class Command(BaseCommand):
    help = 'Flushes and ets up the DB for initial use'

    def handle(self, **options):
        call_command('flush')

        # create admin user
        User.objects.create_superuser(username=env_config['APP_ADMIN_USERNAME'],
                                      email=env_config['APP_ADMIN_EMAIL'],
                                      password=env_config['APP_ADMIN_PASSWORD'])

        create_cards()
        create_game_with_players()
        create_open_game_with_players()
