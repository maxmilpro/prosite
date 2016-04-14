from django.shortcuts import render
from django.views.generic import ListView
from bids.models import Customer

'''
'''

class CustomerList(ListView):
    model = Customer
    template_name = 'bids/customer_list.html'
    context_object_name = 'all_customers'


