import customtkinter
from utils.settings_manager import SettingsManager
from ui.widgets.settings_widget import SettingsWidget


class SettingsPage(customtkinter.CTkFrame):
    page_width = 190
    page_height = 210
    def __init__(self, master):
        super().__init__(master, corner_radius=0)
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=0)
        self.settings_frame = SettingsWidget(self)
        self.save_button = customtkinter.CTkButton(self, text='Save', command=self.save)
        self.settings_frame.grid(row=0, column=0, sticky='news')
        self.save_button.grid(row=1, column=0, sticky='ns', pady=5)

    def save(self) -> None:
        SettingsManager.set_settings(self.settings_frame.get_current_settings())