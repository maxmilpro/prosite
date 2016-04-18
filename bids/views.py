from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView
from django.core.urlresolvers import reverse_lazy, reverse
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

class CustomerCreate(CreateView):
    model = Customer
    fields = ['first_name', 'last_name', 'street', 'city', 'state', 'zip_code', 'email']
    success_url = reverse_lazy('bids:create_project')

class ProjectCreate(CreateView):
    model = Project
    fields = ['title', 'customer']
    success_url = reverse_lazy('bids:create_proposal')

class ProposalCreate(CreateView):
    model = Proposal
    fields = ['project']
    success_url = reverse_lazy('bids:home')

class SectionCreate(CreateView):
    model = Section
    fields = ['proposal', 'title', 'details', 'cost']
    success_url = reverse_lazy('bids:proposal')




