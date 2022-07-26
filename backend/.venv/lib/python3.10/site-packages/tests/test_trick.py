from django.test import TestCase

from ..models.game import Game
from ..models.hand import Hand
from ..models.trick import Trick

from ..utils.create_cards import create_cards

from .fixtures import create_game_with_players


class TrickModelTests(TestCase):

    def setUp(self):
        create_cards()
        self.test_game = create_game_with_players()
        self.test_game.start_game()
        # trump turn stuff
        self.test_hand = self.test_game.active_hand

        self.trick = Trick.objects.create(hand=self.test_hand)
        # self.trick.save()

    def test_play_card(self):
        player = self.test_hand.active_player
        card = player.cards.last()
        self.trick.play_card(player=player, card=card)
        x = 3
        # assert player does not have card.
        # Assert card in trick
        # card winning?

    # def test_deals_5_cards(self):
    #     game = Game.objects.get(pk=1)
    #
    #     a = game.player_set.get(user__username='alice')
    #     new_hand = Hand(game=game, dealer=a)
    #     new_hand.deal()
    #
    #     self.assertIs(a.cards.count(), 5)
