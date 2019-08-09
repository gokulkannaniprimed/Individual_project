from rest_framework import serializers
from .models import Porting,Connection

class PortingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Porting
        fields = (
            'current_mobile_number', 'current_network','upc','requested_date_time','status','circle'
        ) 

class ConnectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Connection
        fields = (
            'first_name', 'last_name','username','city','state','zipcode',' email','password','type'
        ) 