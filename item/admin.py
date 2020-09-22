from django.contrib import admin

from . import models

class CategoryAdmin(admin.ModelAdmin):
  list_display = ['name']

admin.site.register(models.Category, CategoryAdmin)

class ItemAdmin(admin.ModelAdmin):
  list_display = ['name', 'price', 'category']

admin.site.register(models.Item, ItemAdmin)

