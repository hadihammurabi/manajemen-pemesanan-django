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
  transaction = models.Transaction.objects.create()
  transaction_input = json.loads(req.body)
  for item in transaction_input['detail']:
    item_input = item_models.Item.objects.filter(pk=item['item_id']).first()
    detail = models.TransactionDetail.objects.create(
      transaction=transaction,
      item=item_input,
      qty=item['qty'],
      note=item['note']
    )
  serializer = serializers.TransactionSerializer(transaction)
  return JsonResponse(serializer.data, safe=False)
