from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('categories/', include('item.urls_categories')),
    path('items/', include('item.urls')),
    path('admin/', admin.site.urls),
]
