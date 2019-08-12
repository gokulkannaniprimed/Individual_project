from django.urls import path,include
from .import views

urlpatterns=[
     path('message',views.messages,name="messages"),
     path('chat',views.chat,name="chat"),
     path('ticket',views.ticket,name="ticket"),
     path('problems',views.problems,name='problems')
]