from django.conf.urls import url
from bids.views import (CustomerList, HomeView, ProposalView, SectionView, CustomerCreate, 
ProjectCreate, ProposalCreate, SectionCreate, UpdateSection, DocView)


app_name = 'bids'
urlpatterns = [
    url(r'^$', HomeView.as_view(), name='home'),
    url(r'^customers/$', CustomerList.as_view(), name='customers'),
    url(r'^proposal/(?P<pk>[0-9]+)/$', ProposalView.as_view(), name='proposal'),
    url(r'^proposal/section/(?P<pk>[0-9]+)/$', SectionView.as_view(), name='section'),
    url(r'^customer/create/$', CustomerCreate.as_view(), name='create_customer'),
    url(r'^project/create/$', ProjectCreate.as_view(), name='create_project'),
    url(r'^proposal/create/$', ProposalCreate.as_view(), name='create_proposal'),
    url(r'^proposal/(?P<pk>[0-9]+)/section/create/$', SectionCreate.as_view(), name='create_section'),
    url(r'^proposal/section/(?P<pk>[0-9]+)/update/$', UpdateSection.as_view(), name='update_section'),
    url(r'^proposal/(?P<pk>[0-9]+)/final_doc/$', DocView.as_view(), name='doc_view'), 
]