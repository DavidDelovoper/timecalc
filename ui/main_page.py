import asyncio
import customtkinter
from ui.widgets.log_widget import LogWidget
from utils.time_utils import format_time


class MainPage(customtkinter.CTkFrame):
    page_width = 190
    page_height = 210
    def __init__(self, master, callbacks):
        super().__init__(master, corner_radius=0)


        self.grid_rowconfigure(0, weight=0, minsize=100)
        self.grid_rowconfigure(1, weight=1)
        self.grid_rowconfigure(2, weight=0)
        self.grid_columnconfigure(0, weight=1)
        self.time_frame = customtkinter.CTkFrame(self, corner_radius=0)
        self.time_frame.grid_rowconfigure((0,1,2), minsize=32)
        self.time_frame.grid_rowconfigure(3, weight=1)
        self.time_frame.grid(row=0, column=0, sticky='wne')
        self.snap_label = customtkinter.CTkLabel(self.time_frame, text='Snap:')
        self.snap_label.grid(row=0, column=0, sticky='wn', padx=5,)
        self.snap_time_label = customtkinter.CTkLabel(self.time_frame, text='0:00:00.000')
        self.snap_time_label.grid(row=0, column=1, sticky='wn', padx=5)
        self.event1_label = customtkinter.CTkLabel(self.time_frame, text='Event 1:')
        self.event1_label.grid(row=1, column=0, sticky='ws', padx=5)
        self.event1_time_label = customtkinter.CTkLabel(self.time_frame, text='0:00:00.000')
        self.event1_time_label.grid(row=1, column=1, sticky='wn', padx=5)
        self.event2_label = customtkinter.CTkLabel(self.time_frame, text='Event 2:')
        self.event2_label.grid(row=2, column=0, sticky='ws', padx=5)
        self.event2_time_label = customtkinter.CTkLabel(self.time_frame, text='0:00:00.000')
        self.event2_time_label.grid(row=2, column=1, sticky='wn', padx=5)
        self.clipboard_label = customtkinter.CTkLabel(self.time_frame, text='In clipboard:')
        self.clipboard_label.grid(row=3, column=0, sticky='ws', padx=5)
        self.clipboard_value_label = customtkinter.CTkLabel(self.time_frame, text='')
        self.clipboard_value_label.grid(row=3, column=1, sticky='wn', padx=5)
        self.log_widget = LogWidget(self)
        self.log_widget.grid(row=1, column=0, sticky='news')
        self.start_stop_button = customtkinter.CTkButton(self, text='Start', fg_color='green', hover_color='darkgreen', command=self.start_stop)
        self.start_stop_button.grid(row=2, column=0, sticky='n', pady=5, padx=5, columnspan=2)
        self.is_working = False
        self.start_callback = callbacks['start']
        self.stop_callback = callbacks['stop']
    
    def start_stop(self):
        if not self.is_working:
            asyncio.run(self.start_callback())
            self.start_stop_button.configure(text='Stop', fg_color='#737373', hover_color='#c41b1b')
            self.start_stop_button.update()
            self.is_working = True
        else:
            asyncio.run(self.stop_callback())
            self.start_stop_button.configure(text='Start', fg_color='green', hover_color='darkgreen')
            self.start_stop_button.update()
            self.is_working = False

    def update_time_labels(self, snap_time: str, event1_time: str, event2_time: str, clipboard_time: str):
            if snap_time != format_time(0.0): self.snap_time_label.configure(text=snap_time)
            if event1_time != format_time(0.0): self.event1_time_label.configure(text=event1_time)
            if event2_time != format_time(0.0): self.event2_time_label.configure(text=event2_time)
            if clipboard_time != format_time(0.0): self.clipboard_value_label.configure(text=clipboard_time)

    def reset_time_labels(self):
            self.snap_time_label.configure(text='0:00:00.000')
            self.event1_time_label.configure(text='0:00:00.000')
            self.event2_time_label.configure(text='0:00:00.000')
            self.clipboard_value_label.configure(text='')