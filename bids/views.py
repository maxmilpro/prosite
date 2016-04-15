from django.shortcuts import render
from django.views.generic import ListView, DetailView
from bids.models import Customer, Project, Proposal, Section

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

class ProposalView(DetailView):
    model = Proposal
    template_name = 'bids/proposal_view.html'
    #context_object_name = 

class SectionView(DetailView):
    model = Section
    template_name = 'bids/section_view.html'


