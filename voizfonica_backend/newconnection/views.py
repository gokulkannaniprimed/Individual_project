from django.shortcuts import render
from django.http import HttpResponse
from .models import Connection,Porting
from rest_framework.renderers import JSONRenderer
from django.core import serializers
from django.core.mail import send_mail
from django.forms.models import model_to_dict
from .serializers import ConnectionSerializer,PortingSerializer
from django.views.decorators.csrf import csrf_exempt
import json

class JSONResponse(HttpResponse):
    def __init__(self, data, **kwargs):
        content= JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content,**kwargs)

@csrf_exempt
def portin(request):
    portin_data = json.loads(request.body)
    a=Porting(current_mobile_number=portin_data["current_mobile_number"],upc=portin_data["upc"],current_network=portin_data["current_network"],requested_date_time=portin_data["requested_date_time"],status=portin_data["status"],circle=portin_data["circle"])
    a.save()
   

    return JSONResponse("")

@csrf_exempt
def conn(request):
    conn_data = json.loads(request.body)
    c=Connection(first_name=conn_data["first_name"],last_name=conn_data["last_name"],username=conn_data["last_name"],city=conn_data["city"],status=conn_data["status"],circle=conn_data["circle"])
    c.save()
    send_mail(
    'Thank you for contacting voizfonica',
    'Hi' + conn_data["first_name"] + ', \n\nWe have received your connection request. Soon you will recieve a mail ',
    'admin@voizfonica.com',
    ['skandagurunathan.iprimed@gmail.com'],
    fail_silently=True,
)


    
    return JSONResponse("")


# Create your views here.
