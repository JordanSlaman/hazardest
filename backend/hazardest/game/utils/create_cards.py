from ..models.card import Card
from ..models.choices import CardValues, CardSuits


def create_cards():
    cards = [
        Card(suit=suit, value=value)  for suit in CardSuits for value in CardValues
    ]
    Card.objects.bulk_create(cards)
