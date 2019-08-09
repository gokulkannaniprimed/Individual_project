from django.shortcuts import render
from django.http import HttpResponse
from .models import Transactions
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from rest_framework import status
from .serializers import TransactionsSerializer

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
        trans_data = JSONParser().parse(request)
        trans_serializer = TransactionsSerializer(data=trans_data)
        if Transactions_serializer.is_valid():
            Transactions_serializer.save()
            return JSONResponse(Transactions_serializer.data,status=status.HTTP_201_CREATED)
        return JSONResponse(Transactions_serializer.data,status=status.HTTP_400_BAD_REQUEST)










