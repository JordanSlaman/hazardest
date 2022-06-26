from rest_framework import serializers
from rest_framework.validators import UniqueTogetherValidator

from ..models.player import Player


class PlayerSerializer(serializers.HyperlinkedModelSerializer):

    name = serializers.CharField(source='user.username', read_only=True)

    class Meta:
        model = Player
        fields = ['user', 'game', 'name', 'team', 'position']
        validators = [
            UniqueTogetherValidator(
                queryset=Player.objects.all(),
                fields=['user', 'game'],
                message="A user cannot be in a game more than once."
            ),
            UniqueTogetherValidator(
                queryset=Player.objects.all(),
                fields=['team', 'position'],
                message="Player must have their own position on a team."
            )
        ]

    @staticmethod
    def validate_game(game):
        if game.game_full():
            raise serializers.ValidationError("This game is full!")
        return game

    def validate(self, data):
        """
        Check teams and positions do not clash.
        """
        player_set = data['game'].player_set

        team = data['team']
        team_full = player_set.filter(team=team).count() == 2

        if team_full:
            raise serializers.ValidationError("This team is full!")

        position = data['position']
        position_valid = player_set.model.Position.valid_position(team=team, position=position)
        if not position_valid:
            raise serializers.ValidationError("This is not an available position for this team!")

        # the taken team/position being valid is handled by our UniqueTogetherValidator
        return data
