from django.db import models
from django.contrib.auth.models import User


class Player(models.Model):

    def __str__(self):
        return f'Player {self.pk} - {self.user} - {self.game}|{self.position}'

    class Team(models.IntegerChoices):
        ONE = 1
        TWO = 2

    class Position(models.IntegerChoices):
        NORTH = 1
        EAST = 2
        SOUTH = 3
        WEST = 4

        @staticmethod
        def valid_position(team, position):
            valid_team_positions = {
                1: (1, 3),
                2: (2, 4)
            }
            return position in valid_team_positions[team]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    game = models.ForeignKey('Game', on_delete=models.RESTRICT)
    team = models.PositiveSmallIntegerField(choices=Team.choices)
    position = models.PositiveSmallIntegerField(choices=Position.choices)


    # def __init__(self, position):
    #     self.cards = []
    #     self.position = position
    #
    # def __repr__(self):
    #     return self.position
    #
    # def explain(self):
    #     print(f"""
    #     Player in the {self.position} position, it is your turn.
    #     You have the following cards: {Card.pretty_print(self.cards)}
    #     What would you like to do?
    #     """)
    #
    # def cards_left(self):
    #     return len(self.cards)
    #
    # def has_suit(self, suit):
    #     return suit in {c.suit for c in self.cards}
    #
    # def order_up(self, hand):
    #     print(f"""
    #     Player in the {self.position} position, you have been ordered up.
    #     You will be receiving: {hand.revealed}
    #     Your cards are: {Card.pretty_print(self.cards)}
    #     Which card would you like to remove?
    #     """)
    #     self.play_card()  # Throws away
    #     self.cards.append(hand.revealed)
    #     self.sort_cards(hand)
    #     hand.revealed = None
    #
    #     print(f"""
    #     Player in the {self.position} position, your new hand is: {Card.pretty_print(self.cards)}
    #
    #     """)
    #
    # def sort_cards(self, hand):
    #
    #     d = []
    #     c = []
    #     h = []
    #     s = []
    #
    #     while self.cards:
    #         card = self.cards.pop()
    #
    #         if card.suit == 'Diamonds':
    #             d.append(card) if not card.is_left_bauer(hand) else h.append(card)
    #         if card.suit == 'Clubs':
    #             c.append(card) if not card.is_left_bauer(hand) else s.append(card)
    #         if card.suit == 'Hearts':
    #             h.append(card) if not card.is_left_bauer(hand) else d.append(card)
    #         if card.suit == 'Spades':
    #             s.append(card) if not card.is_left_bauer(hand) else c.append(card)
    #
    #     d.sort(key=hand.card_value)
    #     c.sort(key=hand.card_value)
    #     h.sort(key=hand.card_value)
    #     s.sort(key=hand.card_value)
    #
    #     if hand.trump is None or hand.trump == 'Diamonds':
    #         self.cards = d + c + h + s
    #     elif hand.trump == 'Spades':
    #         self.cards = s + d + c + h
    #     elif hand.trump == 'Clubs':
    #         self.cards = c + h + s + d
    #     elif hand.trump == 'Hearts':
    #         self.cards = h + s + d + c
    #
    # def play_card(self):
    #     """
    #     When called asks the player to choose one of their cards, validates the input.
    #     Returns the card popped from the player's hand.
    #     """
    #
    #     if self.cards_left() > 1:
    #         print(f"0-{self.cards_left() - 1} to play a card.")
    #         string = input(PROMPT)
    #
    #         try:
    #             index = int(string)
    #         except ValueError:
    #             print(u"That's not a number.")
    #             return self.play_card()
    #         else:
    #             if index not in range(self.cards_left()):
    #                 print(f"You don't have a card in position {index}")
    #                 return self.play_card()
    #             else:
    #                 return self.cards.pop(index)
    #     else:
    #         print("Playing last card.")
    #         return self.cards.pop()
