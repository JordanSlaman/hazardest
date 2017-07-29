import itertools, random


class Card:

	def __init__(self, suit, value):
		self.suit = suit
		self.value = value

	def __unicode__(self):
		return "{} of {}".format(self.value, self.suit)

class Deck:

	def __init__(self):
		suits = ['Clubs', 'Hearts', 'Spades', 'Diamonds']
		values = ['Ace', 'King', 'Queen', 'Jack', 'Ten', 'Nine']
		self.cards = [Card(suit, value) for suit, value in itertools.product(suits, values)]

	def shuffle(self):
		random.shuffle(self.cards)

deck = Deck()
deck.shuffle()
for card in deck.cards:
	print unicode(card)