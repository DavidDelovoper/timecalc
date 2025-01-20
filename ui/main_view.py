import customtkinter

from ui.main_page import MainPage
from ui.widgets.navbar import Navbar
from ui.settings_page import SettingsPage


class MainView(customtkinter.CTkFrame):
    def __init__(self, master, callbacks: callable):
        super().__init__(master, fg_color='gray', corner_radius=0, height=40, border_width=0)

        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, minsize=40)
        self.grid_rowconfigure(1, weight=1)

        self.navbar = Navbar(self, self.change_page)
        self.navbar.grid(row=0, column=0, sticky='news')

        self.settings_page = SettingsPage(self)
        self.main_page = MainPage(self, callbacks)

        self.current_page = self.main_page
        self.current_page.grid(row=1, column=0, sticky="news")

    def change_page(self, page: str):
        self.current_page.grid_forget()
        if page == "main":
            self.current_page = self.main_page
        elif page == "settings":
            self.current_page = self.settings_page

        self.current_page.grid(row=1, column=0, sticky="news")