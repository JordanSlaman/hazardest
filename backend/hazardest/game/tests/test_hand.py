from django.test import TestCase
from django.contrib.auth.models import User

from ..models.game import Game
from ..models.hand import Hand
from ..models.player import Player

from ..utils.create_cards import create_cards

class HandModelTests(TestCase):
    def setUp(self):

        create_cards()

        for name in ('alice', 'bob', 'charley', 'diane'):
            User.objects.create_user(username=name, email=f'{name}@{name}.org')

        new_game = Game.objects.create(creator=User.objects.get_by_natural_key('alice'))

        for position, test_user in enumerate(User.objects.all()):
            team = 1 if position % 2 else 2  # Kinda silly I guess...
            Player.objects.create(user=test_user, game=new_game, position=position, team=team)


    def test_deals_cards_correctly(self):
        """
        xxx
        """
        game = Game.objects.get(pk=1)

        a = game.player_set.get(user__username='alice')
        new_hand = Hand(game=game, dealer=a)
        new_hand.deal()

        a.cards.all()
        x = 3

        # time = timezone.now() + datetime.timedelta(days=30)
        # future_question = Question(pub_date=time)
        # self.assertIs(future_question.was_published_recently(), False)
