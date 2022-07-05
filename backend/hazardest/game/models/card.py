from django.db import models


class Card(models.Model):

    def __str__(self):
        return f'{self.get_value_display()} of {self.get_suit_display()}'

    class Suit(models.IntegerChoices):
        DIAMONDS = 1
        CLUBS = 2
        HEARTS = 3
        SPADES = 4

    class Value(models.IntegerChoices):
        ACE = 1
        KING = 2
        QUEEN = 3
        JACK = 4
        TEN = 5
        NINE = 6

    RED_SUITS = Suit.DIAMONDS, Suit.HEARTS
    BLACK_SUITS = Suit.CLUBS, Suit.SPADES

    suit = models.IntegerField(choices=Suit.choices)
    value = models.IntegerField(choices=Value.choices)

    def is_red(self):
        return self.suit in self.RED_SUITS

    def is_black(self):
        return not self.is_red()

    # def is_same_colour(self, card):
    #     return (self.is_red() and card.is_red()) or (self.is_black() and card.is_black())

    # def is_trump(self, hand):
    #     return self.suit == hand.trump or self.is_left_bauer(hand)

    # def is_right_bauer(self, hand):
    #     return self.value == 'Jack' and self.suit == hand.trump

    def trump_is_red(self, hand):
        return hand.trump in self.RED_SUITS

    def trump_is_black(self, hand):
        return hand.trump in self.BLACK_SUITS

    # def is_left_bauer(self, hand):
    #     return all([self.value == '',
    #                 self.suit != hand.trump,
    #                 ((self.is_red() and self.trump_is_red(hand)) or (self.is_black() and self.trump_is_black(hand)))])
