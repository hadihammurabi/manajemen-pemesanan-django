from django.db import models

class Category(models.Model):
  name = models.CharField(max_length=255)
  description = models.TextField(blank=True, null=True)

  def __str__(self):
    return self.name

class Item(models.Model):
  name = models.CharField(max_length=255)
  category = models.ForeignKey(Category, on_delete=models.DO_NOTHING, related_name='items')
  description = models.TextField(blank=True, null=True)
  price = models.IntegerField()

  def __str__(self):
    return self.name
