from tkinter import *
from tkinter import font
from tkinter import Tk
from PIL import Image
from pathlib import Path
from src.multi_client import CustomPlayer


for y in range(2):
    x=CustomPlayer('127.0.0.1',5000,f'player{y+1}')
    x.connect_to_host()
    x.start_recv()
