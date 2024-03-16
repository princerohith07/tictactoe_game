"""
WSGI config for gamesite project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
from django.urls import path
import tictactoe_game.routing
from channels.auth import AuthMiddlewareStack

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "gamesite.settings")

application = ProtocolTypeRouter(
    {
        "http": get_wsgi_application(),
        "websocket": AuthMiddlewareStack(URLRouter(tictactoe_game.routing.websocket_urlpatterns)),
    }
)

def application(environ, start_response):
    if environ.get("PATH_INFO").startswith("/ws/"):
        return websocket_application(environ, start_response)
    return application(environ, start_response)
