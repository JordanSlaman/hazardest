import random

from django.db import models
#
from .player import Player
from .card import Card


class Hand(models.Model):

    def __str__(self):
        return f'Hand {self.pk}'

    game = models.ForeignKey('Game', on_delete=models.RESTRICT)
    dealer = models.OneToOneField(Player, related_name='Dealer', null=True, on_delete=models.CASCADE)

    def deal(self):
        cards = list(Card.objects.all())
        random.shuffle(cards)

        for p in self.game.player_set.all():
            for i in range(5):
                p.cards.add(cards.pop())

        revealed_card = cards.pop()
        # kitty = cards


    # def __init__(self, game, players, num_hands_played):
    #     print(u"Dealing new hand.")

        # self.game = game
        # self.players, self.num_hands_played = players, num_hands_played
        # self.dealer = self.players[num_hands_played % 4]
#
#         self.deck = Deck()
#         self.deck.deal(players)
#         self.revealed = self.deck.top_card()
#         self.active_player = self.player_to_left(self.dealer)
#
#         self.trump = None
#         self.trump_turns = []
#         self.current_trick = None
#         self.tricks_played = []
#
#         self.sort_player_cards()
#
#         while not self.is_over():
#             self.explain()
#             if self.trump is None:
#                 self.trump_turns.append(TrumpTurn(self))
#             else:
#                 self.tricks_played.append(Trick(self))
#
#         for p in self.players:
#             p.cards = []
#
#     def is_over(self):
#         end_conditions = [
#             bool([p for p in self.players if p.cards_left() == 0]),  # Players have naturally exhausted their cards.
#             self.num_trump_turns() == 8  # Players could not determine trump
#         ]
#         return any(end_conditions)
#
#     def num_trump_turns(self):
#         return len(self.trump_turns)
#
#     def num_tricks_played(self):
#         return len(self.tricks_played)
#
#     def player_to_left(self, player=None):
#         if player is None:
#             player = self.active_player
#         index = self.players.index(player)
#         return self.players[(index + 1) % 4]
#
#     def explain(self):
#         print(f"""
#         Hand # {self.num_hands_played}
#         Trick # {self.num_tricks_played()}
#         Dealer is: {self.dealer}
#         Trump is: {self.trump}
#         Player is: {self.active_player}
#         """)
#
#     def set_trump(self, trump):
#         self.trump = trump
#         self.sort_player_cards()
#         if self.num_trump_turns() < 4:
#             self.dealer.order_up(self)
#         print(f"Trump suit is now {self.trump}")
#         self.active_player = self.player_to_left(self.dealer)
#
#     def card_value(self, card):
#         value = VALUES.index(card.value)
#
#         if self.trump is not None:
#             if card.is_trump(self):
#                 value += 10
#             if card.is_right_bauer(self):
#                 value += 10
#             if card.is_left_bauer(self):
#                 value += 5
#
#         return value
#
#     def sort_player_cards(self):
#         for p in self.players:
#             p.sort_cards(self)
