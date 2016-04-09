from django.db import models

class Project(models.Model):
    customer_first_name = models.CharField(max_length=25)
    customer_last_name = models.CharField(max_length=25)
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=35)
    state = models.CharField(max_length=2)
    zip_code = models.IntegerField()
