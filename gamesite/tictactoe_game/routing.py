
from channels.routing import ProtocolTypeRouter, URLRouter
from django.urls import path
from channels.auth import AuthMiddlewareStack
from tictactoe_game import consumers

websocket_urlpatterns = [
    path("ws/game_lobby/", consumers.GameLobbyConsumer.as_asgi()),
    path("ws/room/<str:room_id>/", consumers.RoomConsumer.as_asgi()),
]

application = ProtocolTypeRouter(
    {
        "websocket": AuthMiddlewareStack(URLRouter(websocket_urlpatterns)),
    }
)

