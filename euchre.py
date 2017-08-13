import itertools, random

PROMPT = '>>> '
SUITS = ['Diamonds', 'Clubs', 'Hearts', 'Spades']
RED_SUITS = SUITS[::2]
BLACK_SUITS = SUITS[1::2]
VALUES = ['Ace', 'King', 'Queen', 'Jack', 'Ten', 'Nine']


class Card:

    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

    def __unicode__(self):
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

    def is_left_bauer(self, hand):
        return all([self.value == 'Jack',
                    self.suit != hand.trump,
                    ((self.is_red() and hand.trump in RED_SUITS) or (self.is_black() and hand.trump in BLACK_SUITS))])

    @staticmethod
    def pretty_print(list):
        return [card for card in enumerate(map(unicode, list))]


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

    def __unicode__(self):
        return self.position

    def explain(self):
        print u"""
        Player in the {pos} position, it is your turn.
        You have the following cards: {cards}
        What would you like to do?
        """.format(
            pos=self.position,
            cards=Card.pretty_print(self.cards)
        )

    def cards_left(self):
        return len(self.cards)

    def has_suit(self, suit):
        return suit in {c.suit for c in self.cards}

    def order_up(self, hand):
        print u"""
        Player in the {pos} position, you have been ordered up.
        You will be receiving: {revealed}
        Your cards are: {cards}
        Which card would you like to remove?
        """.format(pos=self.position,
                   revealed=unicode(hand.revealed),
                   cards=Card.pretty_print(self.cards))
        self.play_card() # Throws away
        self.cards.append(hand.revealed)
        self.sort_cards(hand)
        hand.revealed = None

        print u"""
        Player in the {pos} position, your new hand is: {cards}

        """.format(pos=self.position,
                   cards=Card.pretty_print(self.cards))

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

        d.sort(cmp=hand.num_compare_cards)
        c.sort(cmp=hand.num_compare_cards)
        h.sort(cmp=hand.num_compare_cards)
        s.sort(cmp=hand.num_compare_cards)

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
            print u"0-{n} to play a card.".format(n=self.cards_left()-1)
            string = raw_input(PROMPT)

            try:
                index = int(string)
            except ValueError:
                print u"That's not a number."
                return self.play_card()
            else:
                if index not in range(self.cards_left()):
                    print u"You don't have a card in position {}".format(index)
                    return self.play_card()
                else:
                    return self.cards.pop(index)
        else:
            print u"Playing last card."
            return self.cards.pop()


class Turn:

    def __init__(self, hand):
        self.hand = hand
        self.explain()
        self.interpret(raw_input(PROMPT))

    def explain(self):
        raise NotImplemented

    def interpret(self, string):
        raise NotImplemented


class TrumpTurn(Turn):

    def is_first_round(self):
        return self.hand.num_trump_turns() < 4

    def explain(self):
        revealed = self.hand.revealed
        print u"""
        We are currently determining the trump suit.
        The revealed card is: {revealed}
        """.format(revealed=unicode(revealed))
        self.hand.active_player.explain()

        if self.is_first_round():
            if self.hand.active_player is self.hand.dealer:
                print u"T to take {trump} as trump. \nP to pass.".format(trump=revealed.suit)
            else:
                print u"O to order up {trump} as trump. \nP to pass.".format(trump=revealed.suit)
        else:
            print u"""S, C, H, D to choose a suit. \nP to pass."""

    def interpret(self, string):
        self.complete = False
        suits = (('Diamonds', 'd', 'D'),
                 ('Clubs', 'c', 'C'),
                 ('Hearts', 'h', 'H'),
                 ('Spades', 's', 'S'))

        valid_input = False

        revealed_suit = self.hand.revealed.suit

        if string in u'pP':
            valid_input = True
            print u"{player} passes".format(player=unicode(self.hand.active_player))
            self.hand.active_player = self.hand.player_to_left()
            self.complete = True
        else:
            if self.is_first_round():
                if string in u'oOtT':
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
                            print u"You already passed on that suit."
                        break

        if not valid_input:
            print u"Bad input: {}".format(string)
        if not self.complete:
            self.interpret(raw_input(PROMPT))


class TrickTurn():


    def __init__(self, hand):
        self.hand = hand
        self.explain()
        self.hand.current_trick.play_card()


    def explain(self):
        cards_played = self.hand.current_trick.cards_played
        trump = self.hand.trump

        if len(cards_played) == 0:
            print u"""
            No cards have been played.
            {trump} is trump.""".format(trump=trump)
        else:
            print u"""
            The following cards have been played: {history}
            {trump} is trump, {lead} was lead.
            """.format(history=self.hand.current_trick.get_cards_played(),
                       trump=trump,
                       lead=cards_played[0][0].suit)
        self.hand.active_player.explain()


class Trick():

    def __init__(self, hand):
        self.cards_played = []
        self.hand = hand
        hand.current_trick = self


        while not self.is_over():
            TrickTurn(hand)

        from operator import itemgetter
        from copy import copy
        sorted_cards = copy(self.cards_played)
        sorted_cards.sort(cmp=hand.num_compare_cards, key=itemgetter(0))
        print u"Hand goes to {}".format(sorted_cards[0][1].position)

    def is_over(self):
        return len(self.cards_played) == 4

    def play_card(self):
        active_player = self.hand.active_player
        is_valid = True

        card = active_player.play_card()

        if len(self.cards_played) > 0:
            asking_suit = self.cards_played[0][0].suit
            if card.suit is not asking_suit and active_player.has_suit(asking_suit):
                print u"Must follow suit!"
                is_valid = False

        if is_valid:
            self.cards_played.append((card, active_player))
            self.hand.active_player = self.hand.player_to_left()
        else:
            active_player.cards.append(card)
            active_player.sort_cards(self.hand)
            self.play_card()

    def get_cards_played(self):
        return [(unicode(c), p.position) for c, p in self.cards_played]


class Hand:

    def __init__(self, game, players, num_hands_played):
        print u"Dealing new hand."

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
            bool([p for p in self.players if p.cards_left() == 0]), # Players have naturally exhausted their cards.
            self.num_trump_turns() == 8                             # Players could not determine trump
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
        print u"""
        Hand # {hand}
        Trick # {tricks}
        Dealer is: {dealer}
        Trump is: {trump}
        Player is: {player}
        """.format(
            hand=self.num_hands_played,
            dealer=unicode(self.dealer),
            trump=self.trump,
            tricks=self.num_tricks_played(),
            player=unicode(self.active_player)
        )

    def set_trump(self, trump):
        self.trump = trump
        self.sort_player_cards()
        if self.num_trump_turns() < 4:
            self.dealer.order_up(self)
        print u"Trump suit is now {}".format(self.trump)
        self.active_player = self.player_to_left(self.dealer)

    def num_compare_cards(self, card1, card2):
        card1_greater = -1
        cards_equal = 0
        card2_greater = 1

        if self.trump is not None:
            # If only one is trump, it wins.
            if card1.is_trump(self) and not card2.is_trump(self):
                return card1_greater
            elif card2.is_trump(self) and not card1.is_trump(self):
                return card2_greater

            # Bauers win.
            if card1.is_right_bauer(self):
                return card1_greater
            if card2.is_right_bauer(self):
                return card2_greater
            if card1.is_left_bauer(self):
                return card1_greater
            if card2.is_left_bauer(self):
                return card2_greater

        # Highest card wins.
        return VALUES.index(card1.value) - VALUES.index(card2.value)


    def sort_player_cards(self):
        for p in self.players:
            p.sort_cards(self)


class Team:

    points = 0

    def __init__(self, players):
        self.players = players


class Game:

    positions = ['North', 'East', 'South', 'West']
    players = [Player(pos) for pos in positions]
    teams = [Team([p for p in players if p.position in positions[::2]]),
             Team([p for p in players if p.position in positions[1::2]])]
    hands_played = []

    def __init__(self):
        while not self.is_over():
            self.hands_played.append(Hand(self, self.players, len(self.hands_played)))


    def is_over(self):
        for t in self.teams:
            if t.points >= 10:
                return True
        return False

Game()
