from rest_framework import serializers

from ..models.game import Game
from .player import PlayerSerializer
from .game_log import GameLogSerializer


class GameSerializer(serializers.HyperlinkedModelSerializer):
    pk = serializers.IntegerField(read_only=True)

    game_state = serializers.CharField(source='get_game_state_display', max_length=100, read_only=True)

    game_log = GameLogSerializer(source='logentry_set',
                                 many=True,
                                 read_only=True,
                                 required=False,
                                 default=GameLogSerializer())

    players = PlayerSerializer(source='player_set',
                               many=True,
                               read_only=True,
                               default=PlayerSerializer())

    player_count = serializers.IntegerField(
        source='player_set.count',
        read_only=True
    )

    class Meta:
        model = Game
        fields = '__all__'
        read_only_fields = ['players', 'team_one_points', 'team_two_points', 'hands_played', 'dealer']
        # fields = ['players']
        validators = [
            # UniqueTogetherValidator(
            #     queryset=Game.objects.all(),
            #     fields=['user', 'game', 'team', 'position'],
            #     message="Player must not have their own position on a team."
            # )
        ]

    # def to_representation(self, instance):
    #     """Convert `game_state` to string."""
    #     ret = super().to_representation(instance)
    #     ret['game_state'] = GameStates.choices ret['game_state']
    #     return ret

    def create(self, validated_data):
        data = validated_data

        data['team_one_points'] = 0
        data['team_two_points'] = 0

        data['hands_played'] = 0
        data['game_state'] = 'WT'
        data['dealer'] = None

        return Game.objects.create(**data)

    # start
    # validate
    # set dealer
    # create hand

    # def update(self, instance, validated_data):
    #     instance.email = validated_data.get('email', instance.email)
    #     instance.content = validated_data.get('content', instance.content)
    #     instance.created = validated_data.get('created', instance.created)
    #     return instance
