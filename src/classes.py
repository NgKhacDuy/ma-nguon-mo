from random import choice

colors=['R','G','B','Y']
symbols=[x for x in '1234567890']
for x in ['wild','+2','+4','skip','rev']:
    symbols.append(x)


class Card:
    def __init__(self,color=-1,symbol=-1):
        if color==-1:
            self.symbol=choice(symbols)
            if symbol in ['+4','W']:
                self.color='Bl'
                self.type='S'
            else:
                self.color=choice(colors)
        else:
            self.symbol=symbol
            self.color=color

    def print_values(self):
        print(f"({self.color}{self.symbol})")

    def get_values(self):
        return self.color,self.symbol

    def matches(self,card2):
        return self.symbol==card2.symbol or self.color==card2.color

class Player:
    def __init__(self):
        self.cards=[Card() for x in range(7)]
        # for x in self.cards:
        #     x.print_values()

    def draw_card(self):
        x_card=Card()
        self.cards.append(x_card)
#
# def start_card():
#     top_card=Card()
#     while top_card.symbol in ['+2','+4','rev','skip','wild']:
#         top_card=Card()
#     return top_card
#
# def special_card(ind,symbol):
#     global players,topcard,i,dir
#     if symbol=='+2':
#         for x in range(2):
#             if ind+dir==-1:
#                 players[(n-1)%n].drawcard()
#             else:
#                 players[(ind+dir)%n].drawcard()
#     if symbol=='+4':
#         color = input("Enter a color to change :")
#         topcard.color = color
#         for x in range(4):
#             players[(ind+dir)%n].drawcard()
#     if symbol=="wild":
#         color=input("Enter a color to change :")
#         topcard.color=color
#     if symbol=='skip':
#         i+=dir
#     if symbol=='rev':
#         if dir==1:
#             dir=-1
#         else:
#             dir=1
# #
# # topcard=start_card()
# #
# # n=int(input('Number of players:'))
# # i=0
# # dir=1
# # players=[Player() for x in range(n)]
# # print("Topcard is ",topcard.get_values())
# #
# # while True:
# #     print(f'Player {(i%n+1)}"s turn')
# #     print([x.get_values() for x in players[i%n].cards])
# #     ch=int(input("1)Play card 2)draw card"))
# #     if ch==1:
# #         ind=int(input("Enter the index of the card to play:"))
# #         current_card=players[i%n].cards[ind-1]
# #         print(current_card.color,current_card.symbol)
# #         if topcard.matches(current_card):
# #             topcard=current_card
# #             if topcard.symbol in ['+2','+4','rev','skip','wild']:
# #                 special_card(i%n,topcard.symbol)
# #             players[i % n].cards.pop(ind - 1)
# #             print("Updated topcard is", topcard.get_values())
# #         else:
# #             print("Player another card!")
# #             i-=dir
# #         if len(players[i%n].cards)==0:
# #             print(f"Player {i+1} won the match!!")
# #             break
# #         i+=dir
# #         if i==-1:
# #             i=n-1
# #     else:
# #         players[i%n].draw_card()
# #
# #
# #
# #
# #
# #
# #
# #
# #
# #
# #
# #
# #
# #
# #
# #
# #
# #
# #
# #
# #
# #
