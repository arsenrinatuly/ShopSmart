
import os
from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
import shopping.routing  

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'settings.base')

application = ProtocolTypeRouter({
    "http": get_asgi_application(),
    "websocket": AuthMiddlewareStack(
        URLRouter(
            shopping.routing.websocket_urlpatterns  
        )
    ),
})
