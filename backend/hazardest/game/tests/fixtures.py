from django.contrib.auth.models import User

from ..models.game import Game
from ..models.hand import Hand
from ..models.player import Player

from ..models.choices import PlayerTeams, PlayerPositions


def create_game_with_players():
    test_players = {
        'alice': {
            'team': PlayerTeams.RED,
            'position': PlayerPositions.NORTH
        },
        'bob': {
            'team': PlayerTeams.BLACK,
            'position': PlayerPositions.EAST
        },
        'charlie': {
            'team': PlayerTeams.RED,
            'position': PlayerPositions.SOUTH
        },
        'diane': {
            'team': PlayerTeams.BLACK,
            'position': PlayerPositions.WEST
        }
    }

    for test_player in test_players.keys():
        User.objects.create_user(username=test_player, email=f'{test_player}@jordanslaman.com')

    new_game = Game.objects.create(creator=User.objects.get_by_natural_key('alice'))

    for test_user in User.objects.filter(username__in=test_players.keys()):
        Player.objects.create(user=test_user,
                              game=new_game,
                              team=test_players[test_user.username]['team'],
                              position=test_players[test_user.username]['position'])

    return new_game


def create_open_game_with_players():
    test_players = {
        'edward': {
            'team': PlayerTeams.RED,
            'position': PlayerPositions.NORTH
        },
        'felicia': {
            'team': PlayerTeams.BLACK,
            'position': PlayerPositions.EAST
        }
    }

    for test_player in test_players.keys():
        User.objects.create_user(username=test_player, email=f'{test_player}@jordanslaman.com')

    new_game = Game.objects.create(creator=User.objects.get_by_natural_key('edward'))

    for test_user in User.objects.filter(username__in=test_players.keys()):
        Player.objects.create(user=test_user,
                              game=new_game,
                              team=test_players[test_user.username]['team'],
                              position=test_players[test_user.username]['position'])

    return new_game

# def create_hand_in_game():
#     game = Game.objects.get(pk=1)
#
#     a = game.player_set.get(user__username='alice')
#     new_hand = Hand(game=game, dealer=a)
#     return new_hand
