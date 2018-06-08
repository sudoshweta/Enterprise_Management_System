from django.db import models
from apps.opportunity.models import Opportunity
from apps.users.models import USER


class MEETING(models.Model):

    description = models.TextField(max_length=1000, blank=True)
    Opportunity = models.ForeignKey(Opportunity, on_delete=models.CASCADE, blank=True)
    date = models.DateField()
    extras = models.ManyToManyField(USER)