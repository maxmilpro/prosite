from django.conf.urls import url
from bids.views import CustomerList, HomeView


app_name = 'bids'
urlpatterns = [
    url(r'^home/$', HomeView.as_view()),
    url(r'^customers/$', CustomerList.as_view())
]