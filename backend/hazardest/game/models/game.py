from django.db import models
from django.contrib.auth.models import User
from django.conf import settings

from .hand import Hand
from .choices import GameStates
from .log_entry import LogEntry


class Game(models.Model):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # self.deal()

    def __str__(self):
        return f'Game {self.pk} - {self.creator} - {self.game_state}'

    creator = models.ForeignKey(User, on_delete=models.RESTRICT)

    created = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)

    game_state = models.CharField(
        max_length=2,
        choices=GameStates.choices,
        default='WT',
        blank=False
    )

    # Options?
    # turn limit timer
    # select dealer?

    # Teams
    team_red_points = models.PositiveSmallIntegerField(default=0)
    team_black_points = models.PositiveSmallIntegerField(default=0)

    # Hands
    hands_played = models.PositiveSmallIntegerField(default=0)
    active_hand = models.ForeignKey(Hand, null=True, related_name='active_hand', on_delete=models.CASCADE)

    def log(self, log_text):
        if settings.DEBUG:
            print(log_text)
        LogEntry.objects.create(game=self, log_text=log_text)

    # Players
    # Magic methods that confirm & validate via reverse lookups?
    def game_full(self):
        return self.player_set.count() == 4

    def join_game(self, player):
        pass

    def start_game(self):
        # assert player preconditions?

        dealer = self.player_set.get(user=self.creator)
        self.active_hand = Hand(game=self, dealer=dealer)
        self.active_hand.save()
        self.game_state = GameStates.IN_PROGRESS
        self.log('Starting new game...')
        self.save()

    def deal_next_hand(self):
        current_dealer = self.active_hand.dealer
        next_dealer = current_dealer.player_to_the_left()
        self.hands_played += 1
        self.active_hand = Hand(game=self, dealer=next_dealer)

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
