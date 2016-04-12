from django.shortcuts import render
from django.views.generic import ListView
from bids.models import Customer

'''
What views should I make?
1. Index of all Projects
2. Index of Sections associated with proposal
3. Form for creating/editing Sections
'''

class CustomerList(ListView):
    model = Customer
    template_name = 'bids/customer_list.html'


