import uuid

from django.db import models


class BaseModel(models.Model):
    """
    BaseModel is the parent model from which the project models inherit.
    """
    LOOKUP_FIELDS = ['id']

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
