import customtkinter

from ui.widgets.key_entry import KeyEntry
from utils.settings_manager import SettingsManager

class SettingsWidget(customtkinter.CTkScrollableFrame):
    def __init__(self, master):
        super().__init__(master, corner_radius=0)
        self.grid_columnconfigure(0, weight=1)
        self._current_settings = SettingsManager.get_settings()
        
        self.snap_bind = customtkinter.StringVar()
        self.event1_bind = customtkinter.StringVar()
        self.event2_bind = customtkinter.StringVar()

        self.binds_frame = customtkinter.CTkFrame(self, border_color='white', border_width=3)
        self.binds_label = customtkinter.CTkLabel(self.binds_frame, text='Binds')
        self.binds_frame.grid_columnconfigure(0, weight=0)
        self.binds_frame.grid_columnconfigure(1, weight=1)
        
        self.snap_bind_label = customtkinter.CTkLabel(self.binds_frame, text='snap')
        self.snap_bind_entry = KeyEntry(self.binds_frame, width=100)

        self.event1_bind_label = customtkinter.CTkLabel(self.binds_frame, text='event 1')
        self.event1_bind_entry = KeyEntry(self.binds_frame, width=100)

        self.event2_bind_label = customtkinter.CTkLabel(self.binds_frame, text='event 2')
        self.event2_bind_entry = KeyEntry(self.binds_frame, width=100)


        self.snap_bind_entry.insert(0, self._current_settings['binds']['snap'])
        self.event1_bind_entry.insert(0, self._current_settings['binds']['event1'])
        self.event2_bind_entry.insert(0, self._current_settings['binds']['event2'])
    
        self.binds_frame.grid(row=0, column=0, sticky='new', padx=5, pady=5)
        self.binds_label.grid(row=0, column=0, sticky='ns', columnspan=2, pady=3)

        self.snap_bind_label.grid(row=1, column=0, sticky='wn', padx=5)
        self.snap_bind_entry.grid(row=1, column=1, sticky='wn', pady=5, padx=5)
        self.event1_bind_label.grid(row=2, column=0, sticky='wn', padx=5)
        self.event1_bind_entry.grid(row=2, column=1, sticky='wn', pady=5, padx=5)
        self.event2_bind_label.grid(row=3, column=0, sticky='wn', padx=5)
        self.event2_bind_entry.grid(row=3, column=1, sticky='wn', pady=5, padx=5)

        self.port = customtkinter.StringVar()

        self.mpc_frame = customtkinter.CTkFrame(self, border_color='white', border_width=3)
        self.mpc_frame.grid_columnconfigure(0, weight=0)
        self.mpc_frame.grid_columnconfigure(1, weight=1)
        self.mpc_frame_label = customtkinter.CTkLabel(self.mpc_frame, text='Media Player Classic')
        self.port_label = customtkinter.CTkLabel(self.mpc_frame, text='port:')
        self.port_entry = customtkinter.CTkEntry(self.mpc_frame, textvariable=self.port, width=100)

        self.port_entry.insert(0, self._current_settings['port'])

        self.mpc_frame.grid(row=1, column=0, sticky='new', padx=5, pady=5)
        self.mpc_frame_label.grid(row=0, column=0, sticky='ns', columnspan=2, pady=3)
        self.port_label.grid(row=1, column=0, sticky='nsw', padx=5, pady=5)
        self.port_entry.grid(row=1, column=1, sticky='nsw', padx=5, pady=5)

        self.save_to_clipboard = customtkinter.BooleanVar(value=self._current_settings['save_to_clipboard'])

        self.extra_frame = customtkinter.CTkFrame(self, border_color='white', border_width=3)
        self.extra_frame.grid_columnconfigure(0, weight=0)
        self.extra_frame.grid_columnconfigure(1, weight=1)
        self.extra_frame_label = customtkinter.CTkLabel(self.extra_frame, text='Extra')
        self.clipboard_label = customtkinter.CTkLabel(self.extra_frame, text='Copy to clipboard:')
        self.clipboard_checkbox = customtkinter.CTkCheckBox(self.extra_frame, variable=self.save_to_clipboard, text='')


        self.extra_frame.grid(row=2, column=0, sticky='new', padx=5, pady=5)
        self.extra_frame_label.grid(row=0, column=0, sticky='ns', columnspan=2, pady=3)
        self.clipboard_label.grid(row=1, column=0, sticky='nsw', padx=5, pady=5)
        self.clipboard_checkbox.grid(row=1, column=1, sticky='nsw', padx=5, pady=5)

    def get_current_settings(self):
        self._current_settings['binds'] = {
            'snap': self.snap_bind_entry.entry_var.get(),
            'event1': self.event1_bind_entry.entry_var.get(),
            'event2': self.event2_bind_entry.entry_var.get()
        }
        self._current_settings['port'] = self.port.get()
        self._current_settings['save_to_clipboard'] = self.save_to_clipboard.get()
        print(self._current_settings)
        return self._current_settings