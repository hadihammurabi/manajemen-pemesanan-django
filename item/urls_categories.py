from django.urls import path

from . import views_categories

urlpatterns = [
    path('', views_categories.index),
]
