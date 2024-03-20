from customtkinter import CTkFrame, CTkEntry, CTkButton

from src.run_clients import RunClient


class LoginFrame(CTkFrame):
    def __init__(self, master):
        CTkFrame.__init__(self, master)
        self.master = master
        self.input = CTkEntry(master=self, placeholder_text="Your name", width=300)
        self.entry = self.input.pack(side="top", fill="y",
                                     pady=10)
        self.btn = CTkButton(master=self, text="Play", corner_radius=32, command=self.validate).pack(
            side="top",
            fill="y")

    def validate(self):
        if self.input.get() != "":
            name = self.input.get()
            print(name)
            self.master.switch_frame("PageWaiting")
            client = RunClient(name=name, master=self.master)
            client.connect()
            # Assuming connect() is a blocking call or you have a way to know when to switch frames


if __name__ == "__main__":
    app = LoginFrame()
    app.mainloop()
