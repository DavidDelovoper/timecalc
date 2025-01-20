import customtkinter

from ui.main_page import MainPage
from ui.settings_page import SettingsPage


class Navbar(customtkinter.CTkFrame):
    def __init__(self, master, change_page_callback):
        super().__init__(master, fg_color='gray', corner_radius=0, height=40, border_width=0)
        self.change_page_callback = change_page_callback

        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, minsize=30, weight=1)
        self.grid_columnconfigure(1, minsize=30, weight=1)


        self.main_button = customtkinter.CTkButton(self, text="Main", command=self.go_main,
                                                    fg_color='transparent', text_color='black',
                                                    corner_radius=0, hover_color='lightgray', width=80)
        self.main_button.grid(row=0, column=0, sticky='nswe')

        self.settings_button = customtkinter.CTkButton(self, text="Settings", command=self.go_settings,
                                                        fg_color='transparent', text_color='black',
                                                        corner_radius=0, hover_color='lightgray', width=80)
        self.settings_button.grid(row=0, column=1, sticky='nwse')

    def go_main(self):
        self.change_page_callback("main")
        self.winfo_toplevel().geometry(f'{MainPage.page_width}x{MainPage.page_height}')

    def go_settings(self):
        self.change_page_callback("settings")
        self.winfo_toplevel().geometry(f'{SettingsPage.page_width}x{SettingsPage.page_height}')