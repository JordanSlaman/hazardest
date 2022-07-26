from django.db import models

from .card import Card
from .hand import Hand
from .player import Player

from .choices import CardSuits


class Trick(models.Model):
    hand = models.ForeignKey(Hand, on_delete=models.CASCADE)

    # Todo not-null when trump determined
    suit_trump = models.IntegerField(null=True, choices=CardSuits.choices)
    suit_lead = models.IntegerField(null=True, choices=CardSuits.choices)

    cards_played = models.ManyToManyField(Card)
    card_winning = models.ForeignKey(Card, related_name='winning_card', null=True, on_delete=models.RESTRICT)
    player_winning = models.ForeignKey(Player, null=True, on_delete=models.RESTRICT)

    # points worth?
    # states? while trick not over? -> less than 4 played

    def play_card(self, player, card):
        # todo leading suit

        active_player = self.hand.active_player

        if not player == active_player:
            raise Exception('Not your turn...')

        # elif trick over -> cards == 4?

        else:
            active_player.cards.remove(card)
            self.cards_played.add(card) # dealing too many somehow

            if self.cards_played.count() == 1 or Card.higher_value(card,
                                                                   self.card_winning,
                                                                   leading_suit=self.suit_lead,
                                                                   trump_suit=self.suit_trump):
                self.card_winning = card
                self.player_winning = active_player

            self.hand.game.log(f'{active_player.user.username} played a {card}.')
            self.hand.game.log(f'{self.player_winning.user.username} is winning the trick with {self.card_winning}.')
            self.active_player = active_player.player_to_the_left()
            self.hand.game.log(f'It is now {active_player.user.username}\'s turn.')
            self.save()

    def compare_cards(self):
        pass

    def update_winner(self):
        pass

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
