from django.conf.urls import url
from bids.views import CustomerList, HomeView

urlpatterns = [
    url(r'^home/$', HomeView.as_view()),
    url(r'^customers/$', CustomerList.as_view())
]