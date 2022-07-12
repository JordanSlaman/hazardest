from django.test import TestCase

from ..models.game import Game
from ..models.hand import Hand

from ..utils.create_cards import create_cards

from .fixtures import create_game_with_players


class HandModelTests(TestCase):
    def setUp(self):
        create_cards()
        self.test_game = create_game_with_players()

    def test_deals_5_cards(self):
        test_dealer = self.test_game.player_set.get(user__username='alice')
        new_hand = Hand(game=self.test_game, dealer=test_dealer)

        for player in self.test_game.player_set.all():
            self.assertIs(player.cards.count(), 5)
