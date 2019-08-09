
from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import auth
from django.views.decorators.csrf import csrf_exempt
import json

@csrf_exempt 

def login(request):
    print(json.loads(request.body))

    if request.method == 'POST':
        req=json.loads(request.body)
        username = req['username']
        password = req['password']
        user = auth.authenticate(username=username, password= password)
        if user is not None:
            auth.login(request,user)
            print("in") 
            return HttpResponse("success")
        else:
            return HttpResponse("failure")  
 
# Create your views here.
