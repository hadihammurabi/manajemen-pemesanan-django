from rest_framework import serializers

from . import models

class CategorySerializer(serializers.ModelSerializer):
  class Meta:
    model = models.Category
    fields = '__all__'

class ItemSerializer(serializers.ModelSerializer):
  category = serializers.StringRelatedField()

  class Meta:
    model = models.Item
    fields = '__all__'
