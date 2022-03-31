"""
Serializer classes for players models.
"""

from rest_framework import serializers
from rest_framework.relations import PrimaryKeyRelatedField

from apps.players.models import Player, Position
from apps.teams.models import Team
from apps.teams.serializers import TeamSerializer


class PositionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Position
        fields = '__all__'


class PlayerSerializer(serializers.ModelSerializer):
    position = PrimaryKeyRelatedField(required=False, many=False, queryset=Position.objects.all())
    team = PrimaryKeyRelatedField(required=False, many=False, queryset=Team.objects.all())

    class Meta:
        model = Player
        fields = '__all__'


class PlayerDetailSerializer(serializers.ModelSerializer):
    position = PositionSerializer(read_only=True, many=False)
    team = TeamSerializer(read_only=True, many=False)

    class Meta:
        model = Player
        fields = '__all__'
