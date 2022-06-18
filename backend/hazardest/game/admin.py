from django.contrib import admin

from .models.game import Game
from .models.player import Player

admin.site.register(Game)
admin.site.register(Player)
