SUITS = ['Diamonds', 'Clubs', 'Hearts', 'Spades']
RED_SUITS = SUITS[::2]
BLACK_SUITS = SUITS[1::2]
VALUES = ['Ace', 'King', 'Queen', 'Jack', 'Ten', 'Nine']


class Team:

    def __init__(self, players):
        self.players = players
        self.points = 0


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
