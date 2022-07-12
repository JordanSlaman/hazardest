from django.contrib import admin

from .models.card import Card
from .models.game import Game
from .models.hand import Hand
from .models.log_entry import LogEntry
from .models.player import Player
from .models.trick import Trick

admin.site.register(Card)
admin.site.register(Game)
admin.site.register(Hand)
admin.site.register(LogEntry)
admin.site.register(Player)
admin.site.register(Trick)
