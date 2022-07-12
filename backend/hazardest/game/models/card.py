from django.db import models

from .choices import CardValues, CardSuits


class Card(models.Model):

    def __str__(self):
        return f'{self.get_value_display()} of {self.get_suit_display()}'

    suit = models.CharField(
        max_length=1,
        choices=CardSuits.choices,
        blank=False
    )

    value = models.SmallIntegerField(
        choices=CardValues.choices,
        blank=False
    )

    def is_red(self):
        return CardSuits.is_red(self.suit)

    def is_black(self):
        return CardSuits.is_black(self.suit)

    def is_same_colour(self, card):
        return (self.is_red() and card.is_red()) or (self.is_black() and card.is_black())

    # def is_trump(self, hand):
    #     return self.suit == hand.trump or self.is_left_bauer(hand)

    # def is_right_bauer(self, hand):
    #     return self.value == 'Jack' and self.suit == hand.trump

    # def trump_is_red(self, hand):
    #     return hand.trump in self.RED_SUITS

    # def trump_is_black(self, hand):
    #     return hand.trump in self.BLACK_SUITS

    # def is_left_bauer(self, hand):
    #     return all([self.value == '',
    #                 self.suit != hand.trump,
    #                 ((self.is_red() and self.trump_is_red(hand)) or (self.is_black() and self.trump_is_black(hand)))])

    @classmethod
    def higher_value(cls, card1, card2, leading_suit, trump_suit):
        x = 4
        pass
