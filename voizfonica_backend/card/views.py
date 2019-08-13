from django.shortcuts import render
from django.http import HttpResponse
from .models import Card
from rest_framework.renderers import JSONRenderer
from django.core import serializers
from .serializers import CardSerializer
from django.views.decorators.csrf import csrf_exempt

class JSONResponse(HttpResponse):
    def __init__(self, data, **kwargs):
        content= JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content,**kwargs)

@csrf_exempt
def getCard(request):
    c=Card.objects.all()
    d=CardSerializer(c, many=True)
    print(d.data)
    return JSONResponse(d.data)

    if request.method == 'POST':  
        j=json.loads(request.body)
        print(j)
        obj=Card(card_holder_name=j['card_holder_name'],card_type=j['card_type'],card_number=j['card_number'],cvv=j['cvv'],card_bank=j['card_bank'],processing_charges=j['processing_charges'])
        obj.save()
        return JSONResponse("success")


