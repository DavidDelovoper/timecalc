import customtkinter


class KeyEntry(customtkinter.CTkEntry):
    def __init__(self, master, width=100):
        self.entry_var = customtkinter.StringVar()
        super().__init__(master, width=width, textvariable=self.entry_var)

        self.bind('<FocusIn>', self.on_focus_in)
        self.bind('<FocusOut>', self.on_focus_out)
    
    def on_focus_in(self, event):
        event.widget.delete(0, customtkinter.END)
        event.widget.bind('<KeyRelease>', self.on_key_release)
        event.widget.bind('<Key>', self.on_key_press)

    def on_focus_out(self, event):
        event.widget.unbind('<Key>')

    def on_key_press(self, event):
        self.entry_var.set('')

    def on_key_release(self, event):
        key = event.keysym.lower()

        if key in ["shift_l", "shift_r", "control_l", "control_r", "alt_l", "alt_r", "win_l", "win_r"]:
            return

        modifiers = []
        if event.state & 0x4:  # Ctrl
            modifiers.append("ctrl")
        if event.state & 0x1:  # Shift
            modifiers.append("shift")
        if event.state & 0x20000:  # Alt
            modifiers.append("alt")
        if event.state & 0x8:  # Win 
            modifiers.append("win")
            
        key_combination = "+".join(modifiers + [key])
        self.entry_var.set(key_combination)