import json

from django.shortcuts import render
from django.http import JsonResponse

from item import models as item_models
from . import models, serializers

def index(req):
  if (req.method == 'POST'):
    return create(req)

  transactions = models.Transaction.objects.all()
  transactions = serializers.TransactionSerializer(transactions, many=True)
  return JsonResponse(transactions.data, safe=False)

def create(req):
  transaction_input = json.loads(req.body)
  transaction = serializers.TransactionSerializer(data=transaction_input)
  if transaction.is_valid():
    transaction.save()
  else:
    print(transaction.errors)
  return JsonResponse(transaction.data, safe=False)
