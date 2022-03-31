import datetime

from django.db.models import Avg, Count
from django.db.models.functions import ExtractYear
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.players.models import Player
from apps.players.serializers import PlayerDetailSerializer
from apps.teams.models import Team, StaffMember, StaffRole
from apps.teams.serializers import (
    StaffRoleSerializer,
    TeamSerializer,
    StaffMemberSerializer,
    StaffMemberDetailSerializer,
)


class TeamView(viewsets.ModelViewSet):
    serializer_class = TeamSerializer
    queryset = Team.objects.all()


class StaffMemberView(viewsets.ModelViewSet):
    serializer_class = StaffMemberSerializer
    queryset = StaffMember.objects.all()

    def get_serializer_class(self):
        """
        Returns custom serializer for StaffMember based on action.

        A more detailed view for retrieve, list actions and more
        """
        if hasattr(self, "action") and (self.action == "create" or self.action == "partial_update"):
            return super(StaffMemberView, self).get_serializer_class()
        else:
            return StaffMemberDetailSerializer


class StaffRoleView(viewsets.ModelViewSet):
    serializer_class = StaffRoleSerializer
    queryset = StaffRole.objects.all()


class StatsView(APIView):
    """
    Class used for serving stats
    """
    def get(self, request, *args, **kwargs):
        data = {}

        data["total_teams"] = Team.objects.count()
        data["total_players"] = Player.objects.count()

        try:
            data["youngest_player"] = PlayerDetailSerializer(Player.objects.latest("date_of_birth")).data
            data["oldest_player"] = PlayerDetailSerializer(Player.objects.earliest("date_of_birth")).data
        except Player.DoesNotExist:
            data["youngest_player"] = None
            data["oldest_player"] = None

        data["total_non_starters"] = Player.objects.filter(is_starter=False).count()

        try:
            data["avg_non_starters"] = (
                    Player.objects.filter(team__isnull=False, is_starter=False).count() / Team.objects.all().count()
            )
        except ZeroDivisionError:
            data["avg_non_starters"] = 0

        try:

            data["team_most_players"] = TeamSerializer(
                Team.objects.annotate(player_count=Count("player")).order_by("-player_count")[0]
            ).data
        except IndexError:
            data["team_most_players"] = None

        try:

            data["avg_age_players"] = Player.objects.filter(date_of_birth__isnull=False).aggregate(
                average_age=Avg(datetime.date.today().year - ExtractYear("date_of_birth"))
            )["average_age"]
        except ZeroDivisionError:
            data["avg_age_players"] = 0

        try:

            data["avg_total_players"] = round(Player.objects.all().count() / Team.objects.all().count(), 2)
        except ZeroDivisionError:
            data["avg_total_players"] = 0

        try:
            data["oldest_coach"] = StaffMemberDetailSerializer(StaffMember.objects.filter(role__name="coach").earliest("date_of_birth")).data
        except StaffMember.DoesNotExist:
            data["oldest_coach"] = None

        return Response(data=data)
