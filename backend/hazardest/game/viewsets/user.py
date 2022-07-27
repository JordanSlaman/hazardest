from django.contrib.auth.models import User, Group

from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework import permissions

from ..serializers.user import UserSerializer, GroupSerializer, ProfileSerializer


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

    @action(detail=False, methods=['get'])
    def active(self, request):
        return Response(UserSerializer(request.user, context={'request': request}).data)

    @action(detail=False, methods=['get'])
    def profile(self, request):
        return Response(ProfileSerializer(request.user.profile, context={'request': request}).data)

    # @action(detail=False, methods=['post'])
    # def login(self, request):
    #     # Important, this sets the session cookie on the response
    #     django_login(request, request.user)
    #     return Response(UserSerializer(request.user, context={'request': request}).data)
    #
    # @action(detail=False, methods=['post'])
    # def logout(self, request):
    #     django_logout(request)
    #     return Response({})


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]
