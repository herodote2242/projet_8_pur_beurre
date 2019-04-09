from django.urls import path, include
from django.contrib import admin


urlpatterns = [
    path('index/', admin.site.urls),
    path('favorites/', include('favorites.urls')),
    path('products/', include('products.urls')),
    path('users/', include('users.urls')),
    path('main/', include('main.urls')),
]
