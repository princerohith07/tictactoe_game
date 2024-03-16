# authentication/models.py
from django.db import models

class Room(models.Model):
    room_name = models.CharField(max_length=100)
    room_id = models.CharField(max_length=100)
    player1 = models.CharField(max_length=100)
    player2 = models.CharField(max_length=100)
    player1_symbol = models.CharField(max_length=1)
    player2_symbol = models.CharField(max_length=1)
    player1_turn = models.BooleanField(default=True)
    player2_turn = models.BooleanField(default=False)
    player1_wins = models.BooleanField(default=False)
    player2_wins = models.BooleanField(default=False)
    draw = models.BooleanField(default=False)
    game_over = models.BooleanField(default=False)
    player1_ready = models.BooleanField(default=False)
    player2_ready = models.BooleanField(default=False)

    def __str__(self):
        return self.room_name

