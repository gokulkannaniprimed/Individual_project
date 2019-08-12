from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from rest_framework import status
from django.core import serializers
from .serializers import ProblemsSerializer,TicketSerializer,ChatSerializer,MessagesSerializer
from .models import Ticket,Problems,Chat,Messages
import json
import datetime

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
          this.messages_display=[
               {
                 sender_type:'user',
                 message_content:'something',
                 time_stamp:'11/08/19 11:17:27 am'
               },
               {
                 sender_type:'bot',
                 message_type:'information',
                 message_content:'something',
                 time_stamp:'11/08/19 11:17:27 am'
               },
               {
                 sender_type:'bot',
                 message_type:'option',
                 message_content:'something',
                 time_stamp:'11/08/19 11:17:27 am'
               }
             ];

@csrf_exempt
def problems(request):
     ProblemsBC=Problems.objects.all()
     ProblemsAC=ProblemsSerializer(ProblemsBC,many=True)
     print(ProblemsAC.data)
     return JSONResponse(ProblemsAC.data)

#@login_required

@csrf_exempt
def messages(request):
     if request.method=='GET':
          MessagesBC=Messages.objects.all()
          MessagesAC=MessagesSerializer(MessagesBC,many=True)
          print(MessagesAC)
          return JSONResponse(MessagesAC.data)

     elif request.method=='POST':
          j=json.loads(request.body)
          print(j)
          obj=Messages(chat_id=j["chat_id"],user_id=j["user_id"],sender_type=j["sender_type"],message_content=j["message_content"],message_type=j["message_type"],time_stamp=j["time_stamp"])
          temp_str=j["message_content"]
          obj.save()
          if 'payment' in temp_str:
               obj=obj=Messages(chat_id=j["chat_id"],user_id="",sender_type="bot",message_content="Please select from below options",message_type="information",time_stamp=str(datetime.datetime.now().strftime("%d-%m-%y %I:%M:%S %p"))) 
               obj.save()
               obj=Messages(chat_id=j["chat_id"],user_id="",sender_type="bot",message_content="Payment failed",message_type="option",time_stamp=str(datetime.datetime.now().strftime("%d-%m-%y %I:%M:%S %p")))
               obj.save()
               obj=Messages(chat_id=j["chat_id"],user_id="",sender_type="bot",message_content="Wrong deduction",message_type="option",time_stamp=str(datetime.datetime.now().strftime("%d-%m-%y %I:%M:%S %p")))
               obj.save()
               obj=Messages(chat_id=j["chat_id"],user_id="",sender_type="bot",message_content="Wrong bill",message_type="option",time_stamp=str(datetime.datetime.now().strftime("%d-%m-%y %I:%M:%S %p")))   
               obj.save()
          return JSONResponse("success")

# @login_required

@csrf_exempt
def chat(request):
     if request.method=='GET':
          ChatBC=Chat.objects.all()
          ChatAC=ChatSerializer(ChatBC,many=True)
          #print(ChatAC.data)
          print(JSONResponse(ChatAC.data))
          return JSONResponse(ChatAC.data)

     elif request.method=='POST':
          j=json.loads(request.body)
          print(j)
          obj=Chat(user_id=j["user_id"],ip_address=j["ip_address"],start_time=j["start_time"])
          obj.save()
          return JSONResponse("success")