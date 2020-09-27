from rest_framework import serializers

from item import models as item_models
from . import models

class TransactionDetailSerializer(serializers.ModelSerializer):
  class Meta:
    model = models.TransactionDetail
    exclude = ['transaction']

class TransactionSerializer(serializers.ModelSerializer):
  detail = TransactionDetailSerializer(many=True)
  class Meta:
    model = models.Transaction
    fields = '__all__'

  def create(self, data):
    transaction = models.Transaction.objects.create()

    detail = data.pop('detail')
    for item in detail:
      detail = models.TransactionDetail.objects.create(
        transaction=transaction,
        item=item['item'],
        qty=item['qty'],
        note=item['note']
      )
    return transaction    
