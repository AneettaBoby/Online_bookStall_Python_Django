from django.urls import path
from LibApp import consumers

websocket_urlpatterns = [
    path('ws/product_status/', consumers.ProductStatusConsumer.as_asgi()),
]
