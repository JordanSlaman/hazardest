import itertools, random

PROMPT = '>>> '

class Card:

    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

    def __unicode__(self):
        return "{} of {}".format(self.value, self.suit)


class Deck:

    def __init__(self):
        suits = ['Diamonds', 'Clubs', 'Hearts', 'Spades']
        values = ['Ace', 'King', 'Queen', 'Jack', 'Ten', 'Nine']
        self.cards = [Card(suit, value) for suit, value in itertools.product(suits, values)]
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

    cards = []

    def __init__(self, position):
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
            cards=[card for card in enumerate(map(unicode, self.cards))]
        )

    def cards_left(self):
        return len(self.cards)


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

    def explain(self):
        print u"""
        We are currently determining the trump suit.
        The revealed card is: {revealed}
        """.format(revealed=unicode(self.hand.revealed))
        self.hand.active_player.explain()
        print """
        S, C, H, D to choose a suit.
        P to pass."""

    def interpret(self, string):
        self.complete = False
        suits = (('Diamonds', 'd', 'D'),
                 ('Clubs', 'c', 'C'),
                 ('Hearts', 'h', 'H'),
                 ('Spades', 's', 'S'))

        valid_input = False
        for suit in suits:
            if string in suit:
                valid_input = True
                self.complete = self.hand.set_trump(suit[0])
        if string in ['p','P']:
            valid_input = True
            print "{player} passes".format(player=unicode(self.hand.active_player))
            self.hand.active_player = self.hand.player_to_left()
            self.complete = True

        if not valid_input:
            print "Bad input."
        if not self.complete:
            self.interpret(raw_input(PROMPT))

class TrickTurn(Turn):

    def explain(self):
        print """
        The following cards have been played: {history}
        """.format(history=self.hand.cards_played)
        self.hand.active_player.explain()
        print """
        0-{n} to play a card.""".format(n=self.hand.active_player.cards_left()-1)

    def interpret(self, string):
        player = self.hand.active_player
        self.complete = False

        if int(string) in range(player.cards_left()-1):
            card = player.cards[int(string)]
            self.complete = self.hand.play_card(card)
        else:
            print "Bad input."

        if not self.complete:
            self.interpret(raw_input(PROMPT))


def Trick():

    def __init__(self, hand):
        self.turn = TrickTurn(hand)


class Hand:

    deck = Deck()
    trump = None
    tricks_played = 0
    cards_played = []

    def __init__(self, players, hands_played):
        self.players, self.hands_played = players, hands_played
        self.dealer = self.players[hands_played % 4]

        self.deck.deal(players)
        self.revealed = self.deck.top_card()
        self.active_player = self.player_to_left(self.dealer)


        while not self.is_over():
            self.explain()
            if self.trump is None:
                TrumpTurn(self)

            self.trick = Trick()
            self.turn = TrickTurn(self)

            self.tricks_played += 1

    def is_over(self):
        end_conditions = [
            bool([p for p in self.players if p.cards_left() == 0]),                             # Players have naturally exhausted their cards.
            self.active_player is self.player_to_left(self.dealer) and self.tricks_played != 0  # Players could not determine trump
        ]
        return any(end_conditions)

    def player_to_left(self, player=None):
        if player is None:
            player = self.active_player
        index = self.players.index(player)
        return self.players[(index + 1) % 4]

    def explain(self):
        print u"""
        Hand # {hand}
        Turn # {turns}
        Dealer is: {dealer}
        Trump is: {trump}
        Player is: {player}
        """.format(
            hand=self.hands_played,
            dealer=unicode(self.dealer),
            trump=self.trump,
            turns=self.tricks_played,
            player=unicode(self.active_player)
        )

    def set_trump(self, trump):
        if self.trump is None and (self.revealed is None or self.revealed.suit == trump):
            self.trump = trump
            print "Trump suit is now {}".format(trump)
            self.active_player = self.player_to_left(self.dealer)
            return True
        else:
            print "You can not set that as trump!"
            return False

    def play_card(self, card):

        # logix

        self.cards_played.append(card)
        self.active_player.cards.remove(card)
        self.active_player = self.player_to_left()
        return True

    # def card_ranking(self):
    #     if not self.trump:
            # asking suit?

class Team:

    points = 0

    def __init__(self, players):
        self.players = players


class Game:
    positions = ['North', 'East', 'South', 'West']
    players = [Player(pos) for pos in positions]
    teams = [Team([p for p in players if p.position in positions[::2]]),
             Team([p for p in players if p.position in positions[1::2]])]
    hands_played = 0

    def __init__(self):
        while not self.is_over():
            self.hand = Hand(self.players, self.hands_played)
            self.hands_played += 1

    def is_over(self):
        for t in self.teams:
            if t.points >= 10:
                return True
        return False


Game()
