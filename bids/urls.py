from django.conf.urls import url
from bids.views import CustomerList, HomeView, ProposalView, SectionView


app_name = 'bids'
urlpatterns = [
    url(r'^home/$', HomeView.as_view()),
    url(r'^customers/$', CustomerList.as_view()),
    url(r'^proposal/(?P<pk>[0-9]+)/$', ProposalView.as_view(), name='proposal'),
    url(r'^proposal/(?P<pk>[0-9]+)/sections/$', SectionView.as_view(), name='section')
]