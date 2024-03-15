from tkinter import *
from tkinter import font
from tkinter import Tk
from PIL import Image
from pathlib import Path


class CardWidget(Frame):
    def set_up_card(self, card_tuple, mode=''):
        # mode can be ''-normal ,'dis'-displaycard ,'big' - Big card
        self.color, self.symbol = card_tuple
        self.color_code={'R':'red','Y':'yellow','B':'blue','G':'green','Bl':'black'}
        self.text_color = 'white'
        self.h, self.w = 100,100
        self.sizer = 40
        self.file_fill='M'
        if mode == 'big':
            self.file_fill=''
            self.sizer = 200
            self.text_color =self.color_code[self.color]
            self.h, self.w = 500, 500
        self.canv = Canvas(self, height=self.h, width=self.w)
        self.canv.pack()
        if mode == 'dis':
            self.img = PhotoImage(
                file = f"{Path().absolute()}\\UNO_cards\\UNOempty.png")
        else:
            self.img = PhotoImage(file=self.decide_file())
        self.canv.create_image(self.h / 2, self.w / 2, image=self.img)

        if self.symbol in '0123456789':
            self.canv.create_text(self.h / 2, self.w / 2, text=self.symbol, fill=self.text_color,
                                  font=font.Font(size=self.sizer))
     # below are newly added lines
        self.playbutton = self.canv.create_rectangle(0,0,self.w,self.h,fill="",outline="",tags="playbutton")
        self.canv.tag_bind("playbutton","<Button-1>",self.card_clicked)

    def card_clicked(self,event):
        self.grid_forget()
        print("card_clicked called!")




    def decide_file(self):
        print(self.symbol)
        z=self.file_fill
        if self.symbol in [str(x) for x in range(100)]:
            return f"{Path().absolute()}\\UNO_cards\\UNO{z}{self.color}.png"
        else:
            print('ee')
            if self.symbol == '+2':
                # return Path().absolute()+f'\\UNO_cards\\UNO{z}{self.color}+2.png'
                return f"{Path().absolute()}\\UNO_cards\\UNO{z}{self.color}+2.png"

            if self.symbol == '+4':
                return f"{Path().absolute()}\\UNO_cards\\UNO{z}+4.png"
            if self.symbol == 'skip':
                return f"{Path().absolute()}\\UNO_cards\\UNO{z}{self.color}skip.png"
            if self.symbol == 'wild':
                return f"{Path().absolute()}\\UNO_cards\\UNO{z}wild.png"
            if self.symbol == 'rev':
                return f"{Path().absolute()}\\UNO_cards\\UNO{z}{self.color}+rev.png"


root = Tk()
# type in code to fix the hieght and width of the root frame

# w = CardWidget(root)
# w.set_up_card(('Y', '2'), mode='big')
# w.pack()
### modified part
sides=['left','right','bottom','top',None]
frames={}
for x in sides:
    frames[x]=Frame(root)
    frames[x].pack(side=x)

for x in ['left','right','top']:
    wid=CardWidget(frames[x])
    wid.set_up_card(('kjsbdvkvb','7'),mode='dis')
    wid.pack()

wid=CardWidget(frames[None])
wid.set_up_card(('B','+2'),mode='big')
wid.pack()

print(frames)
import random
cnt=0
for x1 in range(15):
    color,symbol=random.choice(['R','G','B','Y']),random.choice([str(x) for x in range(10)]+['+2','+4','wild'])
    x=CardWidget(frames['bottom'])
    x.set_up_card((color,symbol))
    if x1==7:
        cnt+=1
    x.grid(row=cnt,column=(x1%7))
### modified part ends
root.mainloop()
