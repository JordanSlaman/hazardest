import itertools
import random

PROMPT = '>>> '
SUITS = ['Diamonds', 'Clubs', 'Hearts', 'Spades']
RED_SUITS = SUITS[::2]
BLACK_SUITS = SUITS[1::2]
VALUES = ['Ace', 'King', 'Queen', 'Jack', 'Ten', 'Nine']


class Card:

    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

    def __repr__(self):
        return "{} of {}".format(self.value, self.suit)

    def is_red(self):
        return self.suit in RED_SUITS

    def is_black(self):
        return self.suit in BLACK_SUITS

    def is_same_colour(self, card):
        return (self.is_red() and card.is_red()) or (self.is_black() and card.is_black())

    def is_trump(self, hand):
        return self.suit == hand.trump or self.is_left_bauer(hand)

    def is_right_bauer(self, hand):
        return self.value == 'Jack' and self.suit == hand.trump

    def trump_is_red(self, hand):
        return hand.trump in RED_SUITS

    def trump_is_black(self, hand):
        return hand.trump in BLACK_SUITS

    def is_left_bauer(self, hand):
        return all([self.value == 'Jack',
                    self.suit != hand.trump,
                    ((self.is_red() and self.trump_is_red(hand)) or (self.is_black() and self.trump_is_black(hand)))])

    @staticmethod
    def pretty_print(list):
        return [card for card in enumerate(list)]


class Deck:

    def __init__(self):
        self.cards = [Card(suit, value) for suit, value in itertools.product(SUITS, VALUES)]
        self.shuffle()

    def shuffle(self):
        random.shuffle(self.cards)

    def top_card(self):
        return self.cards.pop()

    def deal(self, players, qty=5):
        for i in range(qty):
            for p in players:
                p.cards.append(self.top_card())


class Player:

    def __init__(self, position):
        self.cards = []
        self.position = position

    def __repr__(self):
        return self.position

    def explain(self):
        print(f"""
        Player in the {self.position} position, it is your turn.
        You have the following cards: {Card.pretty_print(self.cards)}
        What would you like to do?
        """)

    def cards_left(self):
        return len(self.cards)

    def has_suit(self, suit):
        return suit in {c.suit for c in self.cards}

    def order_up(self, hand):
        print(f"""
        Player in the {self.position} position, you have been ordered up.
        You will be receiving: {hand.revealed}
        Your cards are: {Card.pretty_print(self.cards)}
        Which card would you like to remove?
        """)
        self.play_card()  # Throws away
        self.cards.append(hand.revealed)
        self.sort_cards(hand)
        hand.revealed = None

        print(f"""
        Player in the {self.position} position, your new hand is: {Card.pretty_print(self.cards)}

        """)

    def sort_cards(self, hand):

        d = []
        c = []
        h = []
        s = []

        while self.cards:
            card = self.cards.pop()

            if card.suit == 'Diamonds':
                d.append(card) if not card.is_left_bauer(hand) else h.append(card)
            if card.suit == 'Clubs':
                c.append(card) if not card.is_left_bauer(hand) else s.append(card)
            if card.suit == 'Hearts':
                h.append(card) if not card.is_left_bauer(hand) else d.append(card)
            if card.suit == 'Spades':
                s.append(card) if not card.is_left_bauer(hand) else c.append(card)

        d.sort(key=hand.card_value)
        c.sort(key=hand.card_value)
        h.sort(key=hand.card_value)
        s.sort(key=hand.card_value)

        if hand.trump is None or hand.trump == 'Diamonds':
            self.cards = d + c + h + s
        elif hand.trump == 'Spades':
            self.cards = s + d + c + h
        elif hand.trump == 'Clubs':
            self.cards = c + h + s + d
        elif hand.trump == 'Hearts':
            self.cards = h + s + d + c

    def play_card(self):
        """
        When called asks the player to choose one of their cards, validates the input.
        Returns the card popped from the player's hand.
        """

        if self.cards_left() > 1:
            print(f"0-{self.cards_left() - 1} to play a card.")
            string = input(PROMPT)

            try:
                index = int(string)
            except ValueError:
                print(u"That's not a number.")
                return self.play_card()
            else:
                if index not in range(self.cards_left()):
                    print(f"You don't have a card in position {index}")
                    return self.play_card()
                else:
                    return self.cards.pop(index)
        else:
            print("Playing last card.")
            return self.cards.pop()


class Turn:

    def __init__(self, hand):
        self.hand = hand
        self.explain()
        self.interpret(input(PROMPT))

    def explain(self):
        raise NotImplemented

    def interpret(self, string):
        raise NotImplemented


class TrumpTurn(Turn):

    def is_first_round(self):
        return self.hand.num_trump_turns() < 4

    def explain(self):
        revealed = self.hand.revealed
        print(f"""
        We are currently determining the trump suit.
        The revealed card is: {revealed}
        """)
        self.hand.active_player.explain()

        if self.is_first_round():
            if self.hand.active_player is self.hand.dealer:
                print(f"T to take {revealed.suit} as trump. \nP to pass.")
            else:
                print(f"O to order up {revealed.suit} as trump. \nP to pass.")
        else:
            print("""S, C, H, D to choose a suit. \nP to pass.""")

    def interpret(self, string):
        self.complete = False
        suits = (('Diamonds', 'd', 'D'),
                 ('Clubs', 'c', 'C'),
                 ('Hearts', 'h', 'H'),
                 ('Spades', 's', 'S'))

        valid_input = False

        revealed_suit = self.hand.revealed.suit

        if string in 'pP':
            valid_input = True
            print(f"{self.hand.active_player} passes")
            self.hand.active_player = self.hand.player_to_left()
            self.complete = True
        else:
            if self.is_first_round():
                if string in 'oOtT':
                    valid_input = True
                    self.hand.set_trump(revealed_suit)
                    self.complete = True
            else:
                for suit in suits:
                    if string in suit:
                        valid_input = True
                        chosen_suit = suit[0]
                        if chosen_suit != revealed_suit:
                            self.hand.set_trump(chosen_suit)
                            self.complete = True
                        else:
                            print("You already passed on that suit.")
                        break

        if not valid_input:
            print(f"Bad input: {string}")
        if not self.complete:
            self.interpret(input(PROMPT))


class TrickTurn:

    def __init__(self, hand):
        self.hand = hand
        self.explain()
        self.hand.current_trick.play_card()

    def explain(self):
        cards_played = self.hand.current_trick.cards_played
        trump = self.hand.trump

        if len(cards_played) == 0:
            print(f"""
            No cards have been played.
            {trump} is trump.""")
        else:
            print(f"""
            The following cards have been played: {self.hand.current_trick.get_cards_played()}
            {trump} is trump, {cards_played[0][0].suit} was lead.
            """)
        self.hand.active_player.explain()


class Trick:

    def __init__(self, hand):
        self.cards_played = []
        self.hand = hand
        hand.current_trick = self

        while not self.is_over():
            TrickTurn(hand)

        from copy import copy
        sorted_cards = copy(self.cards_played)
        sorted_cards.sort(key=hand.card_value)
        print(f"Hand goes to {sorted_cards[0][1].position}")

    def is_over(self):
        return len(self.cards_played) == 4

    def play_card(self):
        active_player = self.hand.active_player
        is_valid = True

        card = active_player.play_card()

        if len(self.cards_played) > 0:
            asking_suit = self.cards_played[0][0].suit
            player_has_suit = active_player.has_suit(asking_suit)
            playing_left_as_trump = asking_suit == self.hand.trump and card.is_left_bauer(self)

            if card.suit is not asking_suit:
                if not playing_left_as_trump or player_has_suit:
                    print("Must follow suit!")
                    is_valid = False

        if is_valid:
            self.cards_played.append((card, active_player))
            self.hand.active_player = self.hand.player_to_left()
        else:
            active_player.cards.append(card)
            active_player.sort_cards(self.hand)
            self.play_card()

    def get_cards_played(self):
        return [(c, p.position) for c, p in self.cards_played]


class Hand:

    def __init__(self, game, players, num_hands_played):
        print(u"Dealing new hand.")

        self.game = game
        self.players, self.num_hands_played = players, num_hands_played
        self.dealer = self.players[num_hands_played % 4]

        self.deck = Deck()
        self.deck.deal(players)
        self.revealed = self.deck.top_card()
        self.active_player = self.player_to_left(self.dealer)

        self.trump = None
        self.trump_turns = []
        self.current_trick = None
        self.tricks_played = []

        self.sort_player_cards()

        while not self.is_over():
            self.explain()
            if self.trump is None:
                self.trump_turns.append(TrumpTurn(self))
            else:
                self.tricks_played.append(Trick(self))

        for p in self.players:
            p.cards = []

    def is_over(self):
        end_conditions = [
            bool([p for p in self.players if p.cards_left() == 0]),  # Players have naturally exhausted their cards.
            self.num_trump_turns() == 8  # Players could not determine trump
        ]
        return any(end_conditions)

    def num_trump_turns(self):
        return len(self.trump_turns)

    def num_tricks_played(self):
        return len(self.tricks_played)

    def player_to_left(self, player=None):
        if player is None:
            player = self.active_player
        index = self.players.index(player)
        return self.players[(index + 1) % 4]

    def explain(self):
        print(f"""
        Hand # {self.num_hands_played}
        Trick # {self.num_tricks_played()}
        Dealer is: {self.dealer}
        Trump is: {self.trump}
        Player is: {self.active_player}
        """)

    def set_trump(self, trump):
        self.trump = trump
        self.sort_player_cards()
        if self.num_trump_turns() < 4:
            self.dealer.order_up(self)
        print(f"Trump suit is now {self.trump}")
        self.active_player = self.player_to_left(self.dealer)

    def card_value(self, card):
        value = VALUES.index(card.value)

        if self.trump is not None:
            if card.is_trump(self):
                value += 10
            if card.is_right_bauer(self):
                value += 10
            if card.is_left_bauer(self):
                value += 5

        return value

    def sort_player_cards(self):
        for p in self.players:
            p.sort_cards(self)


class Team:

    def __init__(self, players):
        self.players = players
        self.points = 0


class Game:

    def __init__(self):
        self.positions = ['North', 'East', 'South', 'West']
        self.players = [Player(pos) for pos in self.positions]
        self.teams = [
            Team([p for p in self.players if p.position in self.positions[::2]]),
            Team([p for p in self.players if p.position in self.positions[1::2]])
        ]
        self.hands_played = []

        while not self.is_over():
            self.hands_played.append(Hand(self, self.players, len(self.hands_played)))

    def is_over(self):
        for t in self.teams:
            if t.points >= 10:
                return True
        return False


if __name__ == '__main__':
    Game()
