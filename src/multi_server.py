from socket import socket
from pickle import dumps,loads
from src.classes import Player
from threading import Thread
# this is a server that  is going to handle multiple incoming connections!

# clients=int(input("enter number of max clients: "))
from src.classes import Card


class CustomServer:
    def __init__(self, host, port, mx_clients):
        self.ser_socket = socket()
        self.ser_socket.bind((host, port))
        print("Socket intialised ", (host, port))
        self.mx_clients = mx_clients
        self.n=mx_clients
        self.game_over=False

    def start_server(self):
        self.ser_socket.listen(self.mx_clients)
        self.clients = []
        print("Ready and waiting for connections!")
        while len(self.clients)<self.mx_clients:
            con, addr = self.ser_socket.accept()
            self.clients.append((con, addr))
            print("A Player joined!!", (con, addr))
        print("All players have joined!")

    def ping_socket(self, index):
        ''' The idea of this function is to alert the specific client and get their move'''
        con, addr = self.clients[index]
        con.sendall(dumps([True,self.topcard]))
        # 1 is my own code of saying "it's your move"
        print("Waiting for move for player")
        # make a broadcast wait message to all players here
        data=con.recv(1024)
        data = loads(data)
        print("player data : ",data[0].get_values())
        self.topcard=data[0]
        # process move here
        self.process_player_move(data)


    def broadcast_to_all(self,msg):
        '''This fucntion call send on all the clients we have so far'''
        for con,addr in self.clients:
            con.sendall(dumps(msg))
            #  '0' is my own code of saying "wait" to all the clients we can use any symbol
            # the idea is to minimise the number of characters used so as to reduce data usage

    def process_player_move(self,data):
        if data[-1] is True:
            print(f"Player {self.i} won !!")
            import sys
            sys.exit(0)
        else:
            if data[0].symbol is 'skip':
                self.i+=self.dir
            if data[0].symbol is 'rev':
                self.dir*=-1



    def start_card(self):
        top_card = Card()
        while top_card.symbol in ['+2', '+4', 'rev', 'skip', 'wild']:
            top_card = Card()
        return top_card

    def init_game(self):
        self.topcard = self.start_card()

        # n = int(input('Number of players:'))
        self.i = 0
        self.dir = 1
        self.players = [Player() for x in range(self.n)]
        print("Topcard is ", self.topcard.get_values())
        t=Thread(target=self.start_game)
        t.start()

    def start_game(self):
        while self.game_over is False:
            print(f"Player {self.i%self.mx_clients}'s move!")
            self.ping_socket(self.i%self.mx_clients)
            self.i+=self.dir
            print("End")


server_1=CustomServer('127.0.0.1',5000,2)
# player1=CustomPlayer('127.0.0.1',5000)
server_1.start_server()
server_1.init_game()
# server_1.start_game()











