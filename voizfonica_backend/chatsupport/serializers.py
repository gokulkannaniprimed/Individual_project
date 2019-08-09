from rest_framework import serializers
from .models import Ticket,Problems
# ,Chat,Messages
class ProblemsSerializer(serializers.ModelSerializer):
     class Meta:
          model=Problems
          fields=('__all__')

# class ChatSerializer(serializers.ModelSerializer):
#      class Meta:
#           model=Chat
#           fields=('__all__')

# class MessagesSerializer(serializers.ModelSerializer):
#      class Meta:
#           model=Messages
#           fields=('__all__')

class TicketSerializer(serializers.ModelSerializer):
     class Meta:
          model=Ticket
          fields=('__all__')