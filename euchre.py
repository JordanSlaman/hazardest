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

    def print_turn(self):
        print """
        Player in the {pos} position, it is your turn.
        You have the following cards: {cards}
        What would you like to do?
        0, 1, 2, 3, 4 to play that card
        S, C, H, D to choose a suit.
        - can't yet go alone
        """.format(pos=self.position,
                   cards=[card for card in enumerate(map(unicode, self.cards))])

class Hand:

    def __init__(self, players, dealer):
        self.deck = Deck()
        getnext = self.deck.__next__

        for i in range(5):
            for p in players:
                p.cards.append(getnext())

        self.trump = None
        self.revealed = getnext()
        self.dealer = dealer

        states = ['picking trump', 'playing tricks', 'finished']
        self.state = states[0]


    def execute_turn(self, player):

        if self.state == 'finished':
            exit()

        if self.state == 'picking trump':
            print """
            We are currently determining the trump suit.
            The revealed card is: {revealed}
            The dealer is: {dealer}
            """.format(revealed=unicode(self.revealed),
                       dealer=unicode(self.dealer))

        if self.state == 'playing tricks':
            print """
            We are currently determining the trump suit.
            The revealed card is: {revealed}
            The dealer is: {dealer}
            """.format(revealed=unicode(self.revealed),
                       dealer=unicode(self.dealer))


        player.print_turn()
        self.interpret(raw_input(), player)


    def interpret(self, string, player):
        if string in ['d', 'D']:
            self.set_trump('Diamonds', player)
        elif string in ['c', 'C']:
            self.set_trump('Clubs', player)
        elif string in ['h', 'H']:
            self.set_trump('Hearts', player)
        elif string in ['s', 'S']:
            self.set_trump('Spades', player)
        elif string in ['p','P']:
            pass
        elif int(string) in range(5):
            exit()
            # self.play card
        else:
            print "Invalid input"
            self.interpret(raw_input())

    def set_trump(self, trump, player):
        if self.state == 'picking trump' and (self.revealed is None or self.revealed.suit is trump):
            self.trump = trump
            self.state = 'playing tricks'
            print "Trump suit is now {}".format(trump)
        else:
            print "You can not set that as trump!"

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
        self.turn = 0
        self.hand = Hand(self.players, dealer=self.players[self.turn])

        while not self.is_over():
            self.turn += 1
            self.hand.execute_turn(self.active_player())

    def is_over(self):
        for t in self.teams:
            if t.points >= 10:
                return True
        return False

    def active_player(self):
        return self.players[self.turn % 4]


game = Game()
