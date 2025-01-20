import asyncio
import keyboard

class KeyListener():
    async def listen(self, key: str, callback: callable):
        keyboard.add_hotkey(key, callback)
    
    async def stop_all(self):
        keyboard.unhook_all()
        for task in asyncio.all_tasks():
            task.cancel()
            try:
                await task
            except asyncio.CancelledError:
                pass