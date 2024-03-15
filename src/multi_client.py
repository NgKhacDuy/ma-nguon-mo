from socket import socket
from tkinter import Tk, font
from tkinter import *
from pickle import dumps, loads
from threading import Thread
from threading import Thread
from src.classes import Card

class CustomPlayer:
    # class Player:
    def draw_card(self):
        x_card = Card()
        self.cards.append(x_card)

    def __init__(self,host,port,name):
        self.name=name
        self.x=socket()
        self.host=host
        self.port=port
        self.status=0
        self.cards = [Card() for x in range(7)]
        # for x in self.cards:
        #     x.print_values()
        # status variable determines i the player can play or not play now


    def connect_to_host(self):
        print("connect called!")
        self.x.connect((self.host,self.port))
        print("Connect Success!!")

    def start_recv(self):
        self.t=Thread(target=self.recve)
        self.t.start()

    def recve(self):
        while True:
            # we are expecting to recieve an array of unknown length
            # the first element of the array is wether the client was called or not
            data=loads(self.x.recv(1024))
            self.status=data[0]
            print("status:",self.status)
            if self.status is True:
                print("Got pinged!")
                self.active_function(data)
                # in the above line we have to send the last move and if the player won the game
                self.status=False

    def send_to_server(self,msg):
        self.x.sendall(dumps(msg))
        # pass

    def active_function(self,data):
        self.process_top_card(data[1])
        print(self.name,[x.get_values() for x in self.cards])
        move=1000
        card_played=None
        while move not in range(0,len(self.cards)):
            move=int(input("Enter the index of the card to play"))
            card_played = self.cards[move]
            self.cards.remove(card_played)
            if card_played.symbol in ['wild','+4']:
                color=input('enter a color to change wld to !')
                # use only color codes here R,Y,G,B
                card_played.color=color
        print()
        if card_played.matches(data[1]):
            self.send_to_server([card_played,(len(self.cards) == 0)])
        else:
            print("Invalid card played please try again")
            self.active_function(data)
        # get the input of the user from the UI in this part

    def process_top_card(self,card_tuple):
        if card_tuple.symbol in ['+2','+4']:
            for x in range(int(card_tuple[1])):
                self.draw_card()
        # wild and +4 will be sent as such but with color choice ie ('green','*')
        # '*' denotes any number or ssymbol can be played



#
# x=CustomPlayer('127.0.0.1',5000)
# x.connect_to_host()
# x.start_recv()
# # x.active_function()