from django.shortcuts import render
from django.http import HttpResponse
from .models import Transactions
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from rest_framework import status
from .serializers import TransactionsSerializer
import reportlab
from reportlab.pdfgen import canvas
import json


class JSONResponse(HttpResponse):
    def __init__(self, data, **kwargs):

        #converting python primitive type to json data
        content= JSONRenderer().render(data)

        #adding 'content_type' key to the response header as 'application/json'
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content,**kwargs)

@csrf_exempt
def getTransactions(request):
    if request.method == 'GET':
        #get all plans from db
        trans = Transactions.objects.all()
        #convert python model data into python premitive using serializer
        trans_serializer =  TransactionsSerializer(trans, many = True)
        #return
        return JSONResponse(trans_serializer.data)

    elif request.method == 'POST':
        j=json.loads(request.body)
        print(j)
        obj=Transactions(transaction_amount=j["transaction_amount"],transaction_date_time=j["transaction_date_time"],transaction_state=j["transaction_state"],payment_mode=j["payment_mode"],bank_name=j["bank_name"],wallet_linked=j["wallet_linked"],card_linked=j["card_linked"],refund_status=j['refund_status'],ticket_status=j['ticket_status'])
        obj.save()
        return JSONResponse("success")

    elif request.method=='PUT':
        j=json.loads(request.body)
        print(j)
        obj=Transactions(id=j['id'],transaction_amount=j["transaction_amount"],transaction_date_time=j["transaction_date_time"],transaction_state=j["transaction_state"],payment_mode=j["payment_mode"],bank_name=j["bank_name"],wallet_linked=j["wallet_linked"],card_linked=j["card_linked"],refund_status=j['refund_status'],ticket_status=j['ticket_status'])
        obj.save()
        return JSONResponse("success")









