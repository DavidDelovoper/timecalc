import asyncio
import base64
import tempfile
import zlib
import customtkinter
import pyperclip
from ui.main_view import MainView
from utils.key_listener import KeyListener
from utils.parsers import MPCParser
from utils.settings_manager import SettingsManager
from utils.time_utils import format_time, get_time_difference

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.title("")
        self.window_width = 190
        self.window_height = 210
        self.geometry(f"{self.window_width}x{self.window_height}")

        #Transparent icon
        ICON = zlib.decompress(base64.b64decode('eJxjYGAEQgEBBiDJwZDBy'
    'sAgxsDAoAHEQCEGBQaIOAg4sDIgACMUj4JRMApGwQgF/ykEAFXxQRc='))
        _, ICON_PATH = tempfile.mkstemp()
        with open(ICON_PATH, 'wb') as icon_file:
            icon_file.write(ICON)
        self.iconbitmap(default=ICON_PATH)


        self.window_min_width = 140
        self.window_min_height = 210
        self.minsize(self.window_min_width, self.window_min_height)
        self.callbacks = {
            'start': self.start_callback,
            'stop': self.stop_callback
        }
        self.main_view = MainView(self, self.callbacks)
        self.main_view.pack(fill='both', expand=True)
        port = SettingsManager.get_settings()['port']
        self.parser = MPCParser(url=f'http://localhost:{port}/variables.html')
        self.snap_time = self.event1_time = self.event2_time = self.time_difference = 0.0
        

    async def start_callback(self):
        self.key_listener = KeyListener()
        await self.key_listener.listen(SettingsManager.get_settings()['binds']['snap'], lambda: asyncio.run(self.get_moment_time('Snap')))
        await self.key_listener.listen(SettingsManager.get_settings()['binds']['event1'], lambda: asyncio.run(self.get_moment_time('Event1')))
        await self.key_listener.listen(SettingsManager.get_settings()['binds']['event2'], lambda: asyncio.run(self.get_moment_time('Event2')))

    async def stop_callback(self):
        await self.key_listener.stop_all()
        self.reset_labels()


    async def get_moment_time(self, moment_name: str):
        total_seconds = await self.parser.parse_time()
        match moment_name:
            case 'Snap':
                self.snap_time = total_seconds
                self.event1_time = 0.0
                self.event2_time = 0.0
                self.time_difference = 0.0
                self.reset_labels()
            case 'Event1':
                self.event1_time = total_seconds
                self.time_difference = get_time_difference(self.snap_time, total_seconds)
            case 'Event2':
                self.event2_time = total_seconds
                self.time_difference = get_time_difference(self.event1_time, total_seconds)
        self.copy(self.time_difference)
        time = format_time(total_seconds)
        self.log_time(f'{moment_name}: {time}')
        self.update_labels()

    def log_time(self, time: str):
        self.main_view.main_page.log_widget.log_textbox.log(time)

    def update_labels(self):
        self.main_view.main_page.update_time_labels(format_time(self.snap_time), format_time(self.event1_time), format_time(self.event2_time), self.time_difference)

    def reset_labels(self):
        self.main_view.main_page.reset_time_labels()

    def copy(self, value):
        pyperclip.copy(value)

if __name__ == "__main__":
    app = App()
    app.mainloop()