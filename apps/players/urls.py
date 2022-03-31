"""
URLs for players views.
"""
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from apps.players.views import PositionView, PlayerView


router = DefaultRouter()
router.register("players", PlayerView)
router.register("player-position", PositionView)


urlpatterns = [
    path("", include(router.urls)),
]
