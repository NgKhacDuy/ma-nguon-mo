from customtkinter import CTkFrame, CTkLabel


class WaitingFrame(CTkFrame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master

        # Add widgets for the waiting screen here
        self.label = CTkLabel(master=self, text="Waiting...")
        self.label.place(relx=0.5, rely=0.5, anchor="center")
