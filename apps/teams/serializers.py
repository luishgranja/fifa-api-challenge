"""
Serializer classes for teams models.
"""

from rest_framework import serializers
from django_countries.serializer_fields import CountryField
from rest_framework.relations import PrimaryKeyRelatedField

from apps.teams.models import StaffRole, StaffMember, Team


class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = '__all__'


class StaffRoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = StaffRole
        fields = '__all__'


class StaffMemberDetailSerializer(serializers.ModelSerializer):
    nationality = CountryField()
    role = StaffRoleSerializer(read_only=True, many=False)
    team = TeamSerializer(read_only=True, many=False)

    class Meta:
        model = StaffMember
        fields = '__all__'


class StaffMemberSerializer(serializers.ModelSerializer):
    nationality = CountryField()
    role = PrimaryKeyRelatedField(required=False, many=False, queryset=StaffRole.objects.all())
    team = PrimaryKeyRelatedField(required=False, many=False, queryset=Team.objects.all())

    class Meta:
        model = StaffMember
        fields = '__all__'
