from django.conf.urls import url
from bids.views import CustomerList, HomeView, ProposalView, SectionView, CustomerCreate, ProjectCreate, ProposalCreate


app_name = 'bids'
urlpatterns = [
    url(r'^home/$', HomeView.as_view(), name='home'),
    url(r'^customers/$', CustomerList.as_view(), name='customers'),
    url(r'^proposal/(?P<pk>[0-9]+)/$', ProposalView.as_view(), name='proposal'),
    url(r'^proposal/(?P<pk>[0-9]+)/sections/$', SectionView.as_view(), name='section'),
    url(r'^customer/create/$', CustomerCreate.as_view(), name='create_customer'),
    url(r'^project/create/$', ProjectCreate.as_view(), name='create_project'),
    url(r'^proposal/create/$', ProposalCreate.as_view(), name='create_proposal')
]