import datetime

from django.db import models
from django.utils import timezone

class Project(models.Model):
    customer_first_name = models.CharField(max_length=25)
    customer_last_name = models.CharField(max_length=25)
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=2)
    zip_code = models.IntegerField()

    def __str__(self):
        return self.address

class Proposal(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    #title = project.address
    date_created = models.DateField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

class Section(models.Model):
    proposal = models.ForeignKey(Proposal, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    details = models.TextField(default='')
