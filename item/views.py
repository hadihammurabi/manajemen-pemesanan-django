from django.shortcuts import render
from django.http import JsonResponse

from . import models, serializers

def index(req):
  items = models.Item.objects.all()
  serializer = serializers.ItemSerializer(items, many=True)
  return JsonResponse(serializer.data, safe=False)
