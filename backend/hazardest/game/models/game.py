from django.db import models
from django.contrib.auth.models import User

from .player import Player


class Game(models.Model):

    def __str__(self):
        return f'Game {self.pk} - {self.creator} - {self.game_state}'

    creator = models.ForeignKey(User, on_delete=models.RESTRICT)

    created = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)

    # State
    WAITING = 'WT'
    IN_PROGRESS = 'IP'
    ABANDONED = 'AB'
    OVER = 'OV'

    GAME_STATE_CHOICES = [
        (WAITING, 'Waiting for Players'),
        (IN_PROGRESS, 'In Progress'),
        (ABANDONED, 'Abandoned'),
        (OVER, 'Over')
    ]
    game_state = models.CharField(
        max_length=2,
        choices=GAME_STATE_CHOICES,
        default='WT',
    )

    # Teams
    team_one_points = models.PositiveSmallIntegerField(default=0)
    team_two_points = models.PositiveSmallIntegerField(default=0)

    # team_one_player_north = models.OneToOneField(Player, on_delete=models.CASCADE)
    # team_one_player_south = models.OneToOneField(Player, on_delete=models.CASCADE)
    #
    # team_two_player_east = models.OneToOneField(Player, on_delete=models.CASCADE)
    # team_two_player_west = models.OneToOneField(Player, on_delete=models.CASCADE)

    # Tricks
    tricks_played = models.PositiveSmallIntegerField(default=0)
    dealer = models.OneToOneField(Player, related_name='Dealer', null=True, on_delete=models.CASCADE)

    # Players
    # Magic methods that confirm & validate via reverse lookups?
    def game_full(self):
        return self.player_set.count() == 4

    # def players_full(self):
    #     return self.players
    # Entry.objects.filter(headline__contains='Lennon').count() == 4

    # def __init__(self):
    #     self.positions = ['North', 'East', 'South', 'West']
    #     self.players = [Player(pos) for pos in self.positions]
    #     self.teams = [
    #         Team([p for p in self.players if p.position in self.positions[::2]]),
    #         Team([p for p in self.players if p.position in self.positions[1::2]])
    #     ]
    #     self.hands_played = []
    #
    #     while not self.is_over():
    #         self.hands_played.append(Hand(self, self.players, len(self.hands_played)))
    #
    # def is_over(self):
    #     for t in self.teams:
    #         if t.points >= 10:
    #             return True
    #     return False
