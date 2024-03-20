from tkinter import *
from tkinter import font
from tkinter import Tk
from PIL import Image
from pathlib import Path

from customtkinter import CTkFrame

from src.multi_client import CustomPlayer


class RunClient(CTkFrame):

    def __init__(self, name, master):
        CTkFrame.__init__(self, master)
        self.master = master
        self.name = name

    def connect(self):
        for y in range(1):
            x = CustomPlayer('127.0.0.1', 5000, f'player{self.name}', self.master)
            x.connect_to_host()
            x.start_recv()


if __name__ == '__main__':
    RunClient("Duy").connect()
