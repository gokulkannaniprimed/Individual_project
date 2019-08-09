from django.shortcuts import render
from django.http import HttpResponse
from .models import Users

def login(request):
    if request.method == 'POST':
        username = request.POST["username"]
        password = request.POST["password"]
        user = auth.authenticate(username=username, password= password)
        if user is not None:
            auth.login(request,user)
            return HttpResponse("success")
        else:
            message.error(request,"Invalid Credentials")
            return HttpResponse("failure")

# Create your views here.
