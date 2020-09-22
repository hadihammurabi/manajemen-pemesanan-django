from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from . import models, serializers

def index(req):
  categories = models.Category.objects.all()
  serializer = serializers.CategorySerializer(categories, many=True)
  return JsonResponse(serializer.data, safe=False)
