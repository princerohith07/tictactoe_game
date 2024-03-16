
from django.urls import path
from . import views

urlpatterns = [
    # path("", views.index, name="index"),
    path("", views.home, name="home"),
    path("signin/", views.signin, name="signin"),
    path("register/", views.register, name="register"),
    path("game_lobby/", views.game_lobby, name="game_lobby"),
    path("play_with_bot/", views.play_with_bot, name="play_with_bot"),
    path("multiplayer/", views.multiplayer, name="multiplayer"),

]

