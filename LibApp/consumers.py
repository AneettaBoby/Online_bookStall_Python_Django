# consumers.py

from channels.generic.websocket import AsyncWebsocketConsumer
import json

class ProductStatusConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.channel_layer.group_add(
            'product_status_group',
            self.channel_name
        )
        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(
            'product_status_group',
            self.channel_name
        )

    async def status_message(self, event):
        message = event['message']
        await self.send(text_data=json.dumps({
            'message': message
        }))
