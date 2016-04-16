import datetime

from django.db import models
from django.utils import timezone


class Customer(models.Model):
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)
    street = models.CharField(max_length=100)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=2)
    zip_code = models.IntegerField(null=True)
    email = models.EmailField()
    #add phone number

    def __str__(self):
        full_name = self.first_name + ' ' + self.last_name
        return full_name

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
    def __str__(self):
        title = str(self.date_created)
        return title

    '''def total_cost(self)    
        for section in self.section_set.all():
            cost = section.cost
            total = total + cost'''

class Section(models.Model):
    proposal = models.ForeignKey(Proposal, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    details = models.TextField(default='')
    cost = models.IntegerField(null=True)

    def __str__(self):
        return self.title



