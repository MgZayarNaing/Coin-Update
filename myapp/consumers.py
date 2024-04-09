# myapp/consumers.py

import asyncio
from channels.generic.websocket import AsyncWebsocketConsumer
import datetime

class CountdownConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.timer_task = asyncio.create_task(self.run_timer())
        await self.accept()

    async def disconnect(self, close_code):
        self.timer_task.cancel()

    async def run_timer(self):
        now = datetime.datetime.now()
        minute = now.minute % 5
        minutes = 5 - minute
        seconds = minutes * 60 - now.second
        while True:
            if seconds <= 0:
                await self.send(text_data="0:00")
                await self.send(text_data="start_process")  # Trigger next process
                seconds = 300
            else:
                await self.send(text_data=f"{seconds // 60}:{seconds % 60}")
                #await self.send(text_data=f"{minutes}:{seconds % 60}")
                await asyncio.sleep(1)
                seconds -= 1

    async def receive(self, text_data):
        pass  # Handle incoming messages if needed
