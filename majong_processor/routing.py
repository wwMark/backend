from django.urls import re_path

from . import record_consumer

websocket_urlpatterns = [
    re_path('ws/record/', record_consumer.RecordConsumer.as_asgi()),
]
