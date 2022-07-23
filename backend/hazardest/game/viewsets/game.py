from django.shortcuts import get_object_or_404

from rest_framework import status, viewsets
from rest_framework.decorators import action, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from ..models.game import Game
from ..serializers.game import GameSerializer


class GameViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows games to be viewed or edited.
    """
    queryset = Game.objects.all().order_by('-last_updated')
    serializer_class = GameSerializer

    # List Games
    # def list(self, request):
    #     serializer = GameSerializer(self.queryset, many=True)
    #     return Response(serializer.data)

    # Retrieve Game
    def retrieve(self, request, pk=None):
        game = get_object_or_404(self.queryset, pk=pk)
        serializer = GameSerializer(game, context={'request': request})
        return Response(serializer.data)

    # Create Game
    # @action(detail=True, methods=['post'])
    # @permission_classes([IsAuthenticated])
    # def create(self, request, pk=None):

    # Join Game
    @action(detail=True, methods=['post'])
    @permission_classes([IsAuthenticated])
    def join(self, request, pk=None):
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
    @permission_classes([IsAuthenticated])
    def start_game(self, request, pk=None):
        game = get_object_or_404(self.queryset, pk=pk)
        if not game.game_full():
            return Response({"error": "Game does not have 4 players!"},
                            status=status.HTTP_400_BAD_REQUEST)
        game.game_state = 'IP'

        # deal players hands?
        # randomly assign dealer?

        game.save()
        return Response({'status': 'Game in progress'})
