from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer
import json

class PrivateChatConsumer(WebsocketConsumer):
    def connect(self):
        self.chat_token = self.scope['url_route']['kwargs']['chat_token']
        self.chat_token_name = 'chat_%s' % self.chat_token

        # Join private chat
        async_to_sync(self.channel_layer.group_add)(
            self.chat_token_name,
            self.channel_name
        )

        self.accept()

    def disconnect(self, close_code):
        # Leave private chat
        async_to_sync(self.channel_layer.group_discard)(
            self.chat_token_name,
            self.channel_name
        )

    # Receive message from WebSocket
    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']
        name = text_data_json['name']

        # Send message to private chat
        async_to_sync(self.channel_layer.group_send)(
            self.chat_token_name,
            {
                'type': 'chat_message',
                'message': message,
                'name' : name
            }
        )

    # Receive message from private chat
    def chat_message(self, event):
        message = event['message']
        name = event['name']

        print(message)

        # Send message to WebSocket
        self.send(text_data=json.dumps({
            'message': message,
            'name': name
        }))