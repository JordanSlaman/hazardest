from django.test import TestCase

from ..models.game import Game
from ..models.hand import Hand

from ..utils.create_cards import create_cards

from .fixtures import create_game_with_players


class HandModelTests(TestCase):
    def setUp(self):
        create_cards()
        create_game_with_players()

    def test_deals_5_cards(self):
        game = Game.objects.get(pk=1)

        a = game.player_set.get(user__username='alice')
        new_hand = Hand(game=game, dealer=a)
        new_hand.deal()

        self.assertIs(a.cards.count(), 5)
