from rest_framework import viewsets

from apps.players.models import Position, Player
from apps.players.serializers import PositionSerializer, PlayerSerializer, PlayerDetailSerializer


class PositionView(viewsets.ModelViewSet):
    serializer_class = PositionSerializer
    queryset = Position.objects.all()
    permission_classes = ()


class PlayerView(viewsets.ModelViewSet):
    serializer_class = PlayerSerializer
    queryset = Player.objects.all()
    permission_classes = ()

    def get_serializer_class(self):
        """
        Returns custom serializer for Player based on action.

        A more detailed view for retrieve, list actions and more
        """
        if hasattr(self, 'action') and (self.action == 'create' or self.action == 'partial_update'):
            return super(PlayerView, self).get_serializer_class()
        else:
            return PlayerDetailSerializer
