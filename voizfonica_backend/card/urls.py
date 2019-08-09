from django.conf.urls import url
from card import views

urlpatterns = [
    url(r"^getCard/$", views.getCard),
      #http :8000/plans/ in a new terminal  # in browser 127.0.0.1:8000/plans/
]