from django.db import models
from django.core.validators import MinValueValidator

from item import models as item_models

class Transaction(models.Model):
  created_at = models.DateTimeField(auto_now_add=True)

class TransactionDetail(models.Model):
  item = models.ForeignKey(item_models.Item, on_delete=models.DO_NOTHING, related_name='transactions')
  qty = models.IntegerField(default=0, validators=[MinValueValidator(0)])
  note = models.TextField()
  transaction = models.ForeignKey(Transaction, on_delete=models.CASCADE, related_name='detail')
