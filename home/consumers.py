import json
from channels.generic.websocket import AsyncWebsocketConsumer

class AccidentAlertConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.channel_layer.group_add("alerts", self.channel_name)
        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard("alerts", self.channel_name)

    async def send_alert(self, event):
        # Send text and base64 image data to WebSocket
        await self.send(text_data=json.dumps(event['message']))
