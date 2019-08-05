from django.shortcuts import render
from django.http import HttpResponse
from .models import Plans
from rest_framework.renderers import JSONRenderer
from django.core import serializers
from django.forms.models import model_to_dict

def getPlans(request):
    c=Plans.objects.all()
    d = serializers.serialize("json", c)
    return HttpResponse(d)
