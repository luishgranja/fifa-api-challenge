"""
Database models for teams.
"""

from django.db import models
from django_countries.fields import CountryField

from apps.core.models import BaseModel


class Team(BaseModel):
    """
        Model to store team data
    """
    name = models.CharField(max_length=50, verbose_name='team name')
    picture = models.ImageField(verbose_name='team flag', upload_to='teams', null=True, blank=True)
    badge = models.ImageField(verbose_name='team badge', upload_to='badges', null=True, blank=True)

    def __str__(self):
        return self.name


class StaffRole(BaseModel):
    """
        Helper Model to store staff role data
    """
    name = models.CharField(max_length=50, verbose_name='role name')
    description = models.TextField(blank=True, null=True, max_length=500)

    def __str__(self):
        return self.name


class StaffMember(BaseModel):
    """
       Model to store team staff member data
    """
    first_name = models.CharField('first name', max_length=50)
    last_name = models.CharField('last name', max_length=50)
    date_of_birth = models.DateField('date of birth')
    nationality = CountryField()
    role = models.ForeignKey(to=StaffRole, on_delete=models.SET_NULL, null=True)
    team = models.ForeignKey(to=Team, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
