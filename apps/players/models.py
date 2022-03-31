"""
Database models for players.
"""

from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models

from apps.core.models import BaseModel
from apps.teams.models import Team


class Position(BaseModel):
    name = models.CharField(max_length=50, verbose_name='position name')
    description = models.TextField(blank=True, null=True, max_length=500)

    def __str__(self):
        return self.name


class StarterPlayers(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_starter=True)


class Player(BaseModel):
    picture = models.ImageField(verbose_name='image', upload_to='players', null=True, blank=True)
    first_name = models.CharField(verbose_name='first name', max_length=50)
    last_name = models.CharField(verbose_name='last name', max_length=50)
    date_of_birth = models.DateField(verbose_name='date of birth')
    position = models.ForeignKey(to=Position, on_delete=models.SET_NULL, null=True)
    number = models.IntegerField(
        verbose_name='player number',
        validators=[MinValueValidator(0), MaxValueValidator(99)],
    )
    is_starter = models.BooleanField(default=False)
    team = models.ForeignKey(to=Team, on_delete=models.SET_NULL, null=True)

    objects = models.Manager()
    starters = StarterPlayers()

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    class Meta:
        ordering = ['-created_at']
