from rest_framework import serializers

from . import models

class TransactionSerializer(serializers.ModelSerializer):
  class Meta:
    model = models.Transaction
    fields = '__all__'
