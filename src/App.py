from customtkinter import CTk

from src.login import LoginFrame
from src.waiting_screen import WaitingFrame

pages = {
    "StartPage": LoginFrame,
    "PageWaiting": WaitingFrame
}


class Application(CTk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._frame = None
        self.geometry("800x600")
        self.title("My Application")
        self.switch_frame("StartPage")

    def switch_frame(self, page_name):
        """Destroys current frame and replaces it with a new one."""
        cls = pages[page_name]
        new_frame = cls(master=self)
        if self._frame is not None:
            self._frame.destroy()
        self._frame = new_frame
        self._frame.pack()


if __name__ == "__main__":
    app = Application()
    app.mainloop()
