import datetime

from django.db import models
from django.utils import timezone


class Customer(models.Model):
    firt_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)
    street = models.CharField(max_length=100)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=2)
    zip_code = models.IntegerField()
    email = models.EmailField()
    #add phone number

class Project(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title

class Proposal(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    date_created = models.DateField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    #create total_cost function based on cost of each Section

class Section(models.Model):
    proposal = models.ForeignKey(Proposal, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    details = models.TextField(default='')
    cost = models.IntegerField()


