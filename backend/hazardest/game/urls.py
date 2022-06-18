from django.urls import include, path
from rest_framework import routers

from .viewsets.user import UserViewSet, GroupViewSet
from .viewsets.game import GameViewSet
from .viewsets.player import PlayerViewSet


# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'groups', GroupViewSet)
router.register(r'games', GameViewSet)
router.register(r'players', PlayerViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
