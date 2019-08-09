from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from rest_framework import status
from django.core import serializers
from .serializers import ProblemsSerializer,TicketSerializer
from .models import Ticket,Problems
import json
#,Chat,Messages
# ChatSerializer,MessagesSerializer,
#from django.contrib.auth.decorators import login_required
# Create your views here.
from django.views.decorators.csrf import csrf_exempt

class JSONResponse(HttpResponse):
     def __init__(self,data,**kwargs):
          content=JSONRenderer().render(data)
          kwargs['content_type']='application/json'
          super(JSONResponse,self).__init__(content,**kwargs)

#@login_required
@csrf_exempt
def ticket(request):
     if request.method=='GET':
          TicketBC=Ticket.objects.all()
          TicketAC=TicketSerializer(TicketBC,many=True)
          print(TicketAC)
          return JSONResponse(TicketAC.data)
     
     if request.method=='POST':
          j=json.loads(request.body)
          print(j)
          obj=Ticket(ticket_type=j["ticket_type"],ticket_issue_date=j["ticket_issue_date"],ticket_resolution_proposed_date=j["ticket_resolution_proposed_date"],ticket_resolved_date=j["ticket_resolved_date"],ticket_resolution_response=j["ticket_resolution_response"],ticket_re_action_reason=j["ticket_re_action_reason"],ticket_status=j["ticket_status"],chat=j["chat"])
          obj.save()
          return JSONResponse("success")
          # ticket_data=JSONParser().parse(request)
          # ticket_serializer=TicketSerializer(data=ticket_data)
          # if ticket_serializer.is_valid():
          #      ticket_serializer.save()
          # return JSONResponse(ticket_serializer.data,status=status.HTTP_201_CREATED)
          # return JSONResponse(ticket_serializer.errors,status=status.HTTP_400_BAD_REQUEST)
      

@csrf_exempt
def problems(request):
     ProblemsBC=Problems.objects.all()
     ProblemsAC=ProblemsSerializer(ProblemsBC,many=True)
     print(ProblemsAC)
     return JSONResponse(ProblemsAC.data)

#@login_required
# def messages(request):
#      MessagesBC=Messages.objects.all()
#      MessagesAC=MessagesSerializer(MessagesBC,many=True)
#      print(MessagesAC)
#      return JSONResponse(MessagesAC.data)

# @login_required
# def chat(request):
#      ChatBC=Chat.objects.all()
#      ChatAC=ChatSerializer(ChatBC,many=True)
#      print(ChatAC)
#      return JSONResponse(ChatAC.data)