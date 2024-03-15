from tkinter import *
from tkinter import font
from tkinter import Tk
from PIL import Image
from pathlib import Path



class CardWidget(Frame):
    def set_up_card(self, card_tuple, mode=''):
        # mode can be ''-normal ,'dis'-displaycard ,'big' - Big card
        self.color, self.symbol = card_tuple
        self.text_color = 'white'
        self.h, self.w = 100,100
        self.sizer = 40
        if mode == 'big':
            self.sizer = 200
            # self.text_color = translate the color ir R to red andd Y ti Yello etc
            self.h, self.w = 500, 500
        self.canv = Canvas(self, height=self.h, width=self.w)
        self.canv.pack()
        if mode == 'dis':
            self.img = PhotoImage(
                file=Path().absolute()+f'\\UNO_cards\\UNOempty.png')
        else:
            self.img = PhotoImage(file=self.decide_file())
        self.canv.create_image(self.h / 2, self.w / 2, image=self.img)

        if self.symbol in '0123456789':
            self.canv.create_text(self.h / 2, self.w / 2, text=self.symbol, fill=self.text_color,
                                  font=font.Font(size=self.sizer))
    #  below are newly added lines
    #     self.playbutton = self.canv.create_rectangle(0,0,self.w,self.h,fill="",outline="",tags="playbutton")
    #     self.canv.tag_bind("playbutton","<Button-1>",self.fucked)
    #
    # def fucked(self,event):
    #     self.grid_forget()
    #     print("Don't touch me there you perv!!!")

    def decide_file(self):
        print(self.symbol)
        if self.symbol in [str(x) for x in range(100)]:
            return f'C:\\Users\\Balarubinan\\PycharmProjects\\UNO_game\\src\\UNO_cards\\UNOM{self.color}.png'
        else:
            print('ee')
            if self.symbol == '+2':
                return f'C:\\Users\\Balarubinan\\PycharmProjects\\UNO_game\\src\\UNO_cards\\UNOM{self.color}+2.png'
            if self.symbol == '+4':
                return f'C:\\Users\\Balarubinan\\PycharmProjects\\UNO_game\\src\\UNO_cards\\UNOM+4.png'
            if self.symbol == 'skip':
                return f'C:\\Users\\Balarubinan\\PycharmProjects\\UNO_game\\src\\UNO_cards\\UNOM{self.color}skip.png'
            if self.symbol == 'wild':
                return f'C:\\Users\\Balarubinan\\PycharmProjects\\UNO_game\\src\\UNO_cards\\UNOMwild.png'
            if self.symbol == 'rev':
                return f'C:\\Users\\Balarubinan\\PycharmProjects\\UNO_game\\src\\UNO_cards\\UNOM{self.color}rev.png'


root = Tk()
w = CardWidget(root)
w.set_up_card(('Y', '2'), mode='big')
w.pack()
# ### modified part
# f=Frame(root)
# f.pack(side="bottom")8
# import random
# cnt=0
# for x1 in range(15):
#     color,symbol=random.choice(['R','G','B','Y']),random.choice([str(x) for x in range(10)])
#     x=CardWidget()
#     x.set_up_card((color,symbol))
#     if x1==10:
#         cnt+=1
#     x.grid(row=cnt,column=(x1%10))
### modified part ends
root.mainloop()
