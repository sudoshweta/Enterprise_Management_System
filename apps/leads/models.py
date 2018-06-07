from django.db import models


class LEADS(models.Model):
    contact_number=models.CharField(max_length=45)
    comany_name=models.CharField(max_length=45)
    contact_person=models.BigIntegerField()
    source=models.CharField(max_length=45)
    source_type=models.CharField(max_length=45)
    description=models.CharField(max_length=45)
    email=models.EmailField()
    website=models.CharField(max_length=45)
    assigned_boolean=models.BooleanField()