from django.conf.urls import url
from offers import views

urlpatterns = [
    url(r"^getoffers/$", views.offer_list),  #http :8000/plans/ in a new terminal  # in browser 127.0.0.1:8000/plans/
    url(r"^getoffers/(?P<pk>\d+)/$", views.offer_detail),  #in browser 127.0.0.1:8000/plans/2/
]
