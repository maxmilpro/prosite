from django.shortcuts import render
from django.views.generic import ListView
from bids.models import Customer, Project

'''
'''

class HomeView(ListView):
    model = Project
    template_name = 'bids/home_view.html'
    context_object_name = 'projects'

class CustomerList(ListView):
    model = Customer
    template_name = 'bids/customer_list.html'
    context_object_name = 'all_customers'


