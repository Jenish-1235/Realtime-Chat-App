import json
from channels.generic.websocket import AsyncWebsocketConsumer
from django.contrib.auth.models import User
from django.utils import timezone

# Import sync_to_async to wrap ORM calls
from asgiref.sync import sync_to_async

from .models import Message

class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        """
        Called when the websocket is handshaking.
        """
        # Current logged-in user (already set by AuthMiddlewareStack if user is authenticated)
        self.me = self.scope["user"]

        # The 'other_username' is captured from the URL in routing.py (?P<username>\w+)
        self.other_username = self.scope["url_route"]["kwargs"]["username"]

        # Create a unique group name for the 1-on-1 chat using sorted user names
        user_list = sorted([self.me.username, self.other_username])
        self.room_group_name = f"chat_{user_list[0]}_{user_list[1]}"

        # Print debug info (optional)
        print(f">>>> connect() called. me={self.me}, other={self.other_username}")

        # Join the group
        # NOTE: self.channel_layer is NOT None because you have CHANNEL_LAYERS configured
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )

        # Accept the connection
        await self.accept()

    async def disconnect(self, close_code):
        """
        Called when the socket closes.
        """
        print(f">>>> disconnect() called. me={self.me}, other={self.other_username}")
        # Leave the group
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    async def receive(self, text_data):
        """
        Called when a message is received from the client via WebSocket.
        """
        data = json.loads(text_data)
        message_text = data["message"].strip()

        if not message_text:
            return  # Ignore empty messages

        # Get the other user from the DB (wrap with sync_to_async)
        other_user = await sync_to_async(User.objects.get)(username=self.other_username)

        # Create and save the Message object in the DB (must also be wrapped)
        await sync_to_async(Message.objects.create)(
            sender=self.me,
            receiver=other_user,
            content=message_text,
            timestamp=timezone.now()
        )

        # Broadcast the message to the entire group
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                "type": "chat_message",
                "message": message_text,
                "sender": self.me.username
            }
        )

    async def chat_message(self, event):
        """
        Called when a message is sent to the group.
        We'll forward it to the WebSocket client.
        """
        message = event["message"]
        sender = event["sender"]

        # Send JSON data to the WebSocket
        await self.send(text_data=json.dumps({
            "message": message,
            "sender": sender
        }))
