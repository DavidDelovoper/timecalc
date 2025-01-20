import customtkinter
from PIL import Image

from utils.path_utils import resource_path

class LogWidget(customtkinter.CTkFrame):
    def __init__(self, master):
        super().__init__(master, corner_radius=0)
        self.grid_rowconfigure(0, weight=0)
        self.grid_rowconfigure(1, weight=1)
        self.columnconfigure(0, weight=1)
        self.switch_image_on = customtkinter.CTkImage(Image.open(resource_path('assets/images/arrow.png')), size=(10, 10))
        self.switch_image_off = customtkinter.CTkImage(Image.open(resource_path('assets/images/arrow.png')).rotate(180), size=(10, 10))
        self.switch_button = customtkinter.CTkButton(self, image=self.switch_image_on, text='log', width=40, command=self.log_switch, fg_color='transparent', corner_radius=0, hover_color='gray')
        self.is_log_open = False
        self.switch_button.grid(row=0, column=0, sticky='nw')
        self.log_textbox = self.LogTextbox(self)
        self.root = self.winfo_toplevel()
        self.initial_window_width = self.root.winfo_width()
        self.initial_window_height = self.root.winfo_height()
    
    def resize(self, x, y):
        self.winfo_toplevel().geometry(f"{x}x{y}")

    def log_switch(self):
        if self.is_log_open:
            self.switch_button.configure(image=self.switch_image_on)
            self.log_textbox.grid_forget()
            self.resize(self.initial_window_width, self.initial_window_height)
            self.is_log_open = False
        else:
            self.switch_button.configure(image=self.switch_image_off)
            self.log_textbox.grid(row=1, column=0, sticky='news')
            self.resize(self.initial_window_width, self.initial_window_height+100)
            self.is_log_open = True

    class LogTextbox(customtkinter.CTkTextbox):
        def __init__(self, master):
            super().__init__(master, width=0, height=0, corner_radius=0)
            self.configure(state='disabled')

        def log(self, text: str):
            modifier = ''
            if self.get('1.0', 'end').strip() != '':
                modifier = '\n'
            self.configure(state='normal')
            self.insert('end', f'{modifier}{text}')
            self.see('end')
            print(text)
            self.configure(state='disabled')