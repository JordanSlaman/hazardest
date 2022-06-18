from rest_framework import status, viewsets
from rest_framework import permissions
from rest_framework.decorators import action
from rest_framework.response import Response

from ..models.game import Game
from ..serializers.game import GameSerializer


class GameViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows games to be viewed or edited.
    """
    queryset = Game.objects.all().order_by('-last_updated')
    serializer_class = GameSerializer
    permission_classes = [permissions.IsAuthenticated]

    # Create Game

    # Add Player
    @action(detail=True, methods=['post'])
    def add_player(self, request, pk=None):
        user = self.get_object()
        serializer = GameSerializer(data=request.data)
        # if serializer.is_valid():
        #     user.set_password(serializer.validated_data['password'])
        #     user.save()
        #     return Response({'status': 'password set'})
        # else:
        #     return Response(serializer.errors,
        #                     status=status.HTTP_400_BAD_REQUEST)

    # Start Game
    @action(detail=True, methods=['post'])
    def start_game(self, request, pk=None):
        pass
        # Validate 4 players joined
        # update game state
        # deal players hands?
        # randomly assign dealer
