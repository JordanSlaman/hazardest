from ..models.card import Card


def create_cards():
    cards = [Card(suit=suit, value=value) for value in Card.Value.values for suit in Card.Suit.values]
    Card.objects.bulk_create(cards)
