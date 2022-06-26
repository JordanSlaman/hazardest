from django.db import models

# class Trick:

    # def __str__(self):
    #     return f'Trick {} - Game {self.game}'
    #
    # def __init__(self, hand):
    #     self.cards_played = []
    #     self.hand = hand
    #     hand.current_trick = self
    #
    #     while not self.is_over():
    #         TrickTurn(hand)
    #
    #     from copy import copy
    #     sorted_cards = copy(self.cards_played)
    #     sorted_cards.sort(key=hand.card_value)
    #     print(f"Hand goes to {sorted_cards[0][1].position}")
    #
    # def is_over(self):
    #     return len(self.cards_played) == 4
    #
    # def play_card(self):
    #     active_player = self.hand.active_player
    #     is_valid = True
    #
    #     card = active_player.play_card()
    #
    #     if len(self.cards_played) > 0:
    #         asking_suit = self.cards_played[0][0].suit
    #         player_has_suit = active_player.has_suit(asking_suit)
    #         playing_left_as_trump = asking_suit == self.hand.trump and card.is_left_bauer(self)
    #
    #         if card.suit is not asking_suit:
    #             if not playing_left_as_trump or player_has_suit:
    #                 print("Must follow suit!")
    #                 is_valid = False
    #
    #     if is_valid:
    #         self.cards_played.append((card, active_player))
    #         self.hand.active_player = self.hand.player_to_left()
    #     else:
    #         active_player.cards.append(card)
    #         active_player.sort_cards(self.hand)
    #         self.play_card()
    #
    # def get_cards_played(self):
    #     return [(c, p.position) for c, p in self.cards_played]