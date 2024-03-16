
from channels.generic.websocket import WebsocketConsumer
import random
import string
from .models import Room
import json

class RoomConsumer(WebsocketConsumer):
    def connect(self):
        self.accept()

    def disconnect(self, close_code):
        pass

    def receive(self, text_data):
        data = json.loads(text_data)
        if data['action'] == 'create_room':
            self.create_room()
        elif data['action'] == 'join_room':
            self.join_room(data['room_id'])

    def create_room(self):
        room_id = ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))
        room = Room.objects.create(room_name=room_id, room_id=room_id)
        self.send(text_data=f"Room created with id: {room_id}")

    def join_room(self, room_id):
        room = Room.objects.get(room_id=room_id)
        if room.player1 == '':
            room.player1 = 'player1'
            room.save()
            self.send(text_data=f"Joined room {room_id} as player1")
        elif room.player2 == '':
            room.player2 = 'player2'
            room.save()
            self.send(text_data=f"Joined room {room_id} as player2")
        else:
            self.send(text_data=f"Room {room_id} is full")

            