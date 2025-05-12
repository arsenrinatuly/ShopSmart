
from channels.generic.websocket import AsyncWebsocketConsumer
import json


class ListConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.list_id = self.scope['url_route']['kwargs']['list_id']
        self.group_name = f'list_{self.list_id}'
        await self.channel_layer.group_add(self.group_name, self.channel_name)
        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(self.group_name, self.channel_name)

    async def receive(self, text_data):
        data = json.loads(text_data)
        action = data.get('action')
        item_id = data.get('item_id')
        item_name = data.get('item_name')

        if action == 'add':
            await self.channel_layer.group_send(
                self.group_name,
                {
                    'type': 'send_update',
                    'action': 'add',
                    'item_id': item_id,
                    'item_name': item_name,
                    'is_bought': False
                }
            )
        elif action == 'toggle':
            is_bought = await self.get_item_status(item_id)
            await self.channel_layer.group_send(
                self.group_name,
                {
                    'type': 'send_update',
                    'action': 'toggle',
                    'item_id': item_id,
                    'is_bought': not is_bought  
                }
            )
        elif action == 'delete':
            await self.channel_layer.group_send(
                self.group_name,
                {
                    'type': 'send_update',
                    'action': 'delete',
                    'item_id': item_id
                }
            )

    async def send_update(self, event):

        await self.send(text_data=json.dumps({
            'action': event['action'],
            'item_id': event['item_id'],
            'item_name': event.get('item_name'),
            'is_bought': event.get('is_bought', False)  
        }))

    async def get_item_status(self, item_id):
        return False  
