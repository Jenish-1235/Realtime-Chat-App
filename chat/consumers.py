import json
from channels.generic.websocket import AsyncWebsocketConsumer
from django.contrib.auth.models import User
from .models import Message
from django.utils import timezone

class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        # We’ll use the URL route (e.g. /ws/chat/<username>/ ) to figure out the chat group
        self.user_to_chat = self.scope['url_route']['kwargs']['username']
        self.group_name = f'chat_{self.scope["user"].username}_{self.user_to_chat}'
        
        # Join room group
        await self.channel_layer.group_add(self.group_name, self.channel_name)
        await self.accept()

    async def disconnect(self, close_code):
        # Leave room group
        await self.channel_layer.group_discard(self.group_name, self.channel_name)

    # Receive message from WebSocket
    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']

        sender = self.scope["user"]
        receiver_username = self.user_to_chat
        receiver = User.objects.get(username=receiver_username)

        # Save message in the database
        msg = Message.objects.create(
            sender=sender,
            receiver=receiver,
            content=message,
            timestamp=timezone.now()
        )

        # Send message to room group
        await self.channel_layer.group_send(
            self.group_name,
            {
                'type': 'chat_message',
                'message': message,
                'sender': sender.username,
            }
        )

    # Receive message from room group
    async def chat_message(self, event):
        message = event['message']
        sender = event['sender']

        # Send message to WebSocket
        await self.send(text_data=json.dumps({
            'message': message,
            'sender': sender
        }))
