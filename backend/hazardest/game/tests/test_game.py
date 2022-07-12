from django.test import TestCase

from ..utils.create_cards import create_cards
from ..models.log_entry import LogEntry
from .fixtures import create_game_with_players


class GameModelTests(TestCase):
    def setUp(self):
        create_cards()
        self.test_game = create_game_with_players()

    # def test_add_player_full(self):
    # def test_add_player_invalid_position(self):

    def test_logging(self):
        test_string = 'Logging a thing!'
        self.test_game.log(test_string)

        latest_log = LogEntry.objects.filter(game=self.test_game).order_by('-timestamp')[0]
        self.assertEqual(latest_log.log_text, test_string)

    def test_start_game(self):
        self.test_game.start_game()
        self.assertEqual(self.test_game.game_state, 'IP')

    def test_deal_hand(self):
        self.test_game.start_game()
        self.test_game.deal_next_hand()
