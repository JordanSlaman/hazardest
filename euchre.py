import itertools, random


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

    def __next__(self):
        return self.cards.pop()

    def shuffle(self):
        random.shuffle(self.cards)


class Player:

    def __init__(self, position):
        self.position = position
        self.cards = []

    def __unicode__(self):
        return self.position

    def explain(self):
        print """
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
        self.interpret(raw_input())

    def explain(self):
        raise NotImplemented

    def interpret(self, string):
        raise NotImplemented


class TrumpTurn(Turn):

    def explain(self):
        print """
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
            self.complete = True

        if not valid_input:
            print "Bad input."
        if not self.complete:
            self.interpret(raw_input())

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
            self.interpret(raw_input())

class Hand:

    def __init__(self, players, hands_played):
        self.players, self.hands_played = players, hands_played
        self.dealer = self.players[hands_played % 4]

        self.deck = Deck()
        next_card = self.deck.__next__

        for i in range(5):
            for p in players:
                p.cards.append(next_card())

        self.trump = None
        self.revealed = next_card()

        self.active_player = self.player_to_left(self.dealer)
        self.turns_played = 0
        self.cards_played = []

        while not self.is_over():
            self.explain()

            if self.trump is None:
                self.turn = TrumpTurn(self)
            else:
                self.turn = TrickTurn(self)

            self.turns_played += 1
            self.active_player = self.player_to_left(self.active_player)

    def is_over(self):
        end_contitions = [bool([p for p in self.players if p.cards_left() == 0]), # Players have naturally exhausted their cards.
                          ]# self.active_player is self.player_to_left(self.dealer) and self.turns_played != 0] # Players could not determine trump.

        return any(end_contitions)

    def player_to_left(self, player):
        index = self.players.index(player)
        return self.players[(index + 1) % 4]

    def explain(self):
        print """
        Hand # {hand}
        Turn # {turns}
        Dealer is: {dealer}
        Trump is: {trump}
        Player is: {player}
        """.format(
            hand=self.hands_played,
            dealer=unicode(self.dealer),
            trump=self.trump,
            turns=self.turns_played,
            player=unicode(self.active_player)
        )

    def set_trump(self, trump):
        if self.trump is None and (self.revealed is None or self.revealed.suit == trump):
            self.trump = trump
            print "Trump suit is now {}".format(trump)
            self.active_player = self.dealer
            return True
        else:
            print "You can not set that as trump!"
            return False

    def play_card(self, card):

        # logix

        self.cards_played.append(card)
        self.active_player.cards.remove(card)
        return True

    # def card_ranking(self):
    #     if not self.trump:
            # asking suit?

class Team:

    def __init__(self, players):
        self.players = players
        self.points = 0


class Game:

    def __init__(self):
        self.positions = ['North', 'East', 'South', 'West']
        self.players = [Player(position) for position in self.positions]
        self.teams = [Team([p for p in self.players if p.position in self.positions[::2]]),
                      Team([p for p in self.players if p.position in self.positions[1::2]])]
        self.hands_played = 0

        while not self.is_over():
            self.hand = Hand(self.players, self.hands_played)
            self.hands_played += 1

    def is_over(self):
        for t in self.teams:
            if t.points >= 10:
                return True
        return False


game = Game()
