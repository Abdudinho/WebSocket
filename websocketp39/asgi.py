import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "websocketp39.settings")

from django.core.asgi import get_asgi_application
django_asgi_app = get_asgi_application()   # bu Django'ni to'liq sozlaydi (django.setup())

# Faqat SHUNDAN KEYIN modellarga bog'liq narsalarni import qiling
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
import apps.routing

application = ProtocolTypeRouter({
    "http": django_asgi_app,
    "websocket": AuthMiddlewareStack(
        URLRouter(apps.routing.websocket_urlpatterns)
    ),
})