from django.shortcuts import render
from django.http import HttpResponse
from .models import Card
from rest_framework.renderers import JSONRenderer
from django.core import serializers
from .serializers import CardSerializer


class JSONResponse(HttpResponse):
    def __init__(self, data, **kwargs):
        content= JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content,**kwargs)


def getCard(request):
    c=Card.objects.all()
    d=CardSerializer(c, many=True)
    print(d.data)
    return JSONResponse(d.data)


