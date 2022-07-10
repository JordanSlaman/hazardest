from django.contrib.auth.models import User

from ..models.game import Game
from ..models.player import Player


def create_game_with_players():
    for name in ('alice', 'bob', 'charley', 'diane'):
        User.objects.create_user(username=name, email=f'{name}@{name}.org')

    new_game = Game.objects.create(creator=User.objects.get_by_natural_key('alice'))

    for position, test_user in enumerate(User.objects.all()):
        # Kinda silly I guess, I don't love these team/position enums...

        position += 1
        team = 1 if position % 2 else 2

        Player.objects.create(user=test_user, game=new_game, position=position, team=team)

    return new_game
