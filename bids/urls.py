from django.conf.urls import url
from bids.views import CustomerList

urlpatterns = [ 
    url(r'^customers/$', CustomerList.as_view())
]