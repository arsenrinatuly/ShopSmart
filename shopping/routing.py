from django.urls import re_path
from . import consumers

websocket_urlpatterns = [
    re_path(r'ws/shopping/(?P<list_id>[a-f0-9-]+)/$', consumers.ListConsumer.as_asgi()),
]