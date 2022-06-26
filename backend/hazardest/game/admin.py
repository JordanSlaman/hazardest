from django.contrib import admin

from .models.game import Game
from .models.hand import Hand
from .models.log_entry import LogEntry
from .models.player import Player

admin.site.register(Game)
admin.site.register(Hand)
admin.site.register(LogEntry)
admin.site.register(Player)
