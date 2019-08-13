from rest_framework import serializers
from .models import Ticket,Chat,Messages

class ChatSerializer(serializers.ModelSerializer):
     class Meta:
          model=Chat
          fields=('__all__')

class MessagesSerializer(serializers.ModelSerializer):
     class Meta:
          model=Messages
          fields=('__all__')

class TicketSerializer(serializers.ModelSerializer):
     class Meta:
          model=Ticket
          fields=('__all__')