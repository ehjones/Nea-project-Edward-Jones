import turtle
import time
import random
import sys
#from tkinter import *
#import tkinter.font as font

#import tkinter as tk
start_x = -225
player_score = 0
dealer_score = 0
# Create classes
pen = turtle.Turtle()
pen.speed(0)
pen.hideturtle()

class Card():
    def __init__(self, name, suit):
        self.name = name
        self.suit = suit
        self.symbols = {"D":"♦", "C":"♣", "H":"♥", "S":"♠"}
        
    #def print_card(self):
     #   print(f"{self.name}{self.symbols[self.suit]}")
    def __repr__(self):
        return " of ".join((self.name, self.suit))    
        print("SSS")
        print(self.suit)
    def render(self, x, y, pen):
        # Draw border
        pen.penup()
        pen.goto(x, y)
        pen.color("white")
        pen.goto(x-50, y+75)
        pen.begin_fill()
        pen.pendown()
        pen.goto(x+50, y+75)
        pen.goto(x+50, y-75)
        pen.goto(x-50, y-75)
        pen.goto(x-50, y+75)
        pen.end_fill()
        pen.penup()
        
        if self.name != "" and self.suit == "D" or self.suit == "H":
            # Draw suit in the middle
            pen.color("red")
            pen.goto(x-18, y-30)
            pen.write(self.symbols[self.suit], False, font=("Courier New", 48, "normal"))
            
            # Draw top left 
            pen.goto(x-40, y+45)
            pen.write(self.name, False, font=("Courier New", 18, "normal"))
            pen.goto(x-40, y+25)
            pen.write(self.symbols[self.suit], False, font=("Courier New", 18, "normal"))
            
            # Draw bottom right
            pen.goto(x+30, y-60)
            pen.write(self.name, False, font=("Courier New", 18, "normal"))
            pen.goto(x+30, y-80)
            pen.write(self.symbols[self.suit], False, font=("Courier New", 18, "normal"))


        elif self.name != "" and self.suit == "C" or self.suit == "S":
            # Draw suit in the middle
            pen.color("black")
            pen.goto(x-18, y-30)
            pen.write(self.symbols[self.suit], False, font=("Courier New", 48, "normal"))
            
            # Draw top left 
            pen.goto(x-40, y+45)
            pen.write(self.name, False, font=("Courier New", 18, "normal"))
            pen.goto(x-40, y+25)
            pen.write(self.symbols[self.suit], False, font=("Courier New", 18, "normal"))
            
            # Draw bottom right
            pen.goto(x+30, y-60)
            pen.write(self.name, False, font=("Courier New", 18, "normal"))
            pen.goto(x+30, y-80)
            pen.write(self.symbols[self.suit], False, font=("Courier New", 18, "normal"))




class Deck():
    def __init__(self):
        self.cards = [Card(n, s) for n in ["A", "K", "Q", "J", "9", "8", "7", "6", "5", "4", "3", "2"] for s in ["D", "C", "H", "S"]]
        #card = Card(name, suit)
        #self.cards = []
        #names = ("A", "K", "Q", "J", "9", "8", "7", "6", "5", "4", "3", "2")
        #suits = ("D", "C", "H", "S")
        #self.value = 0
        #for name in names:
            #for suit in suits:
                
                #card = Card(name, suit)
                
                #self.cards.append(card)
                #self.shuffle()

# after the cards have been created add value
   

    #def shuffle(self):
        #random.shuffle(self.cards)
        #return card
    
    
    def shuffle(self):
        if len(self.cards) > 1:
          random.shuffle(self.cards)
          print(self.cards)
          
    def get_card(self):
      self.shuffle()
       
      if len(self.cards) > 1:
       return self.cards.pop(0)
       print(self.cards)
       #return card
        
    def reset(self):
        self.cards = [Card(n, s) for n in ["A", "K", "Q", "J", "9", "8", "7", "6", "5", "4", "3", "2"] for s in ["D", "C", "H", "S"]]

        
        
        
        
        
        
        
      
        #self.cards = []
        
        #names = ("A", "K", "Q", "J", "T", "9", "8", "7", "6", "5", "4", "3", "2")
        #suits = ("D", "C", "H", "S")
        
        #for name in names:
            #for suit in suits:
                #card = Card(name, suit)
                #self.cards.append(card)


      
                
        self.shuffle()

class Score:
   def __init__(self, dealer=False):
      self.player_cards = []
      self.dealer_cards = []
      self.value = 0
      self.dealer = dealer
      self.i = 0

   def reset(self):
     self.player_cards = []
     self.dealer_cards = []   

   def player_add_card(self, card):
      print("qq")
      self.player_cards.append(card)
      print(self.player_cards)
      
   
   def dealer_add_card(self, card):
      self.dealer_cards.append(card)
      #card = self.cards.pop()
   
   
   
   def calculate_value(self):
      go = Game_over()
      self.value = 0
      has_ace = False
      print("ii")
      print(self.player_cards)
      for card in self.player_cards:
         print(self.value)
         print("jj")
         if card.name.isnumeric():
            self.value += int(card.name)
            #print(self.value)
         elif card.name == "A":
             self.value += 11
             has_ace = True
         else:
            self.value += 10
      if has_ace == True and self.value == 21:
           go.play_again_win_blackjack() 
            
         

   def get_value(self):
        self.calculate_value()
        print(self.value)
        return self.value
   
   def calculate_value_dealer(self):
      go = Game_over()
      self.value = 0
      has_ace = False
      print("ii")
      print(self.dealer_cards)
      for card in self.dealer_cards:
         print(self.value)
         print("jj")
         if card.name.isnumeric():
            self.value += int(card.name)
            #print(self.value)
         elif card.name == "A":
             self.value += 11
             has_ace = True
         else:
            self.value += 10
      if has_ace == True and self.value == 21:
           go.play_again_lost_blackjack() 
            
        
         

   def get_value_dealer(self):
        self.calculate_value_dealer()
        print(self.value)
        return self.value
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   def display_dealer(self):
       x = 1
       #print(self.cards)
       for card in self.dealer_cards[1:]:
           while x == 1:
            pen = turtle.Turtle()
        
            pen.hideturtle()
            pen.hideturtle()
            pen.penup()
            pen.goto(-150, 275)
            pen.color("blue")
            pen.speed(0)
            pen.begin_fill()
            pen.pendown()
            pen.forward(100)
            pen.right(90) 
            pen.forward(150)
            pen.right(90)
            pen.forward(100)
            pen.right(90) 
            pen.forward(150)
        #pen.left(90)
        #pen.forward(10)
        #pen.left(90)
        #pen.forward(10)
            pen.end_fill()  
            x = x+1
           
           print(self.dealer_cards)
           print(card)
           if x ==2:
               x = x
               self.return_card_dealer(card, x)
           else:
               
               x = x+1
               self.return_card_dealer(card, x)

   def return_card_dealer(self, card, x):
    print("b")
    print(card)
    
        
    while x == 2 :
        card.render(start_x + x * 125, 200, pen)

        time.sleep(1)
        x = x +1


   def display_player(self):
       x = 0
       #print(self.cards)
       for card in self.player_cards:
            
            print(self.player_cards)
            print(card)
            x = x+1
            self.return_card_player(card, x)
       self.player_cards = self.player_cards
   
   def display_dealer_stick(self):
       x = 0
       #print(self.cards)
       for card in self.dealer_cards:
            
            print(self.dealer_cards)
            print(card)
            x = x+1
            self.return_card_dealer_stick(card, x)

   def return_card_dealer_stick(self, card, x):
    print("b")
    print(card)
        
    card.render(start_x + x * 125, 200, pen)

    time.sleep(1)




   def return_card_player(self, card, x):
      
      print("p")
      print(card)
      card.render(start_x + x * 125, 0, pen)

      time.sleep(1)

   def display_player_twist(self, x, y, player_score):
      x = 3
      for card in self.player_cards:
      
       self.return_card_player(card, x) 
       print("yy")
       #return(card)
       
       x = x+1
   
   
   



class Game:
    def __init__(self, player_score, dealer_score, player_score_num):
        #g = Game(player_score, dealer_score, player_score_num)
        self.player_score = Score()
        self.dealer_score = Score()
        self.player_score_num = 0
        self.dealer_score_num = 0
        self.deck = Deck()
        #self.g = Game(player_score, dealer_score, player_score_num)
        #self.player_cards = []
    
    def __repr__(self):
      return self.player_score_num
      return self.dealer_score_num
    
    def set_player_score(self, player_score):
      go = Game_over()
      print("tttx")
      self.score = Score()
      #self.player_score = player_score
      print(self.player_score_num)
      #self.player_score = Score(self.player_score_num)
      #print(self.player_score.get_value())
      #player_score = self.player_score.get_value()
      #self.player_score_num = self.player_score_num + self.player_score.get_value()
      #self.player_score_num = self.player_score_num + self.player_score.get_value()
      self.player_score_num = self.player_score.get_value()
      #self.player_score_num = self.player_score_num + self.player_score
      #self.player_score = self.player_score_num
      print("asda")
      if self.player_score_num > 21:
        go.play_again_lost()
      print(self.player_score_num)
      return self.player_score_num
    
    def get_player_score(self, player_score):
      go = Game_over()
      #self.set_player_score(player_score)
      print("AAAA")
      print(self.player_score_num)
      if self.player_score_num > 21:
        go.play_again_lost()
      return self.player_score_num

    def set_dealer_score(self, dealer_score):
      print("tttx")
      self.score = Score()
      #self.player_score = player_score
      print(self.dealer_score_num)
      #self.player_score = Score(self.player_score_num)
      #print(self.player_score.get_value())
      #player_score = self.player_score.get_value()
      #self.player_score_num = self.player_score_num + self.player_score.get_value()
      #self.player_score_num = self.player_score_num + self.player_score.get_value()
      self.dealer_score_num = self.dealer_score.get_value_dealer()
      #self.player_score_num = self.player_score_num + self.player_score
      #self.player_score = self.player_score_num
      print("asda")
      print(self.dealer_score_num)
      return self.dealer_score_num
    
    def get_dealer_score(self, dealer_score):
      #self.set_player_score(player_score)
      print("AAAA")
      print(self.dealer_score_num)
      return self.dealer_score_num



    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    def play(self, x, y):
        s = Score()
        
        d = Deck()
        s.reset()
        self.player_score = Score()
        self.dealer_score = Score()
        CURSOR_SIZE = 20
        FONT_SIZE = 12
        FONT = ('Arial', FONT_SIZE, 'bold')
        wn = turtle.Screen()
        wn.bgcolor("green")
        wn.setup(800, 600)
#wn.title("Deck of Cards Simulator by @TokyoEdtech")
#twist = Button(wn, text = "Twist")
#twist.pack()
#twist.place(x=700, y=550)
           
        #g = Game(player_score, dealer_score, player_score_num)
        pen = turtle.Turtle()
        pen.color("green")
        pen.speed(0)
        pen.hideturtle()
        pen.hideturtle()
        pen.begin_fill()
#pen.forward(-250)
        pen.forward(550)
        pen.left(90) 
        pen.forward(300)
        pen.left(90)
        pen.forward(800)
        pen.left(90) 
        pen.forward(800)
        pen.left(90)
        pen.forward(800)
        pen.left(90)
        pen.forward(1000)
        pen.end_fill()

        pen.hideturtle()
        button = turtle.Turtle()
        button.hideturtle()
        button.shape('square')
        button.fillcolor('red')
        button.penup()
        button.goto(200,-200)
        button.write("Twist", align='center', font=FONT)
        button.sety(-200+ CURSOR_SIZE + FONT_SIZE)
        
        button.onclick(self.player_twist)
        
        button.showturtle()

        #g = Game(player_score, dealer_score, player_score_num)
        #s = Score()
        pen = turtle.Turtle()
        pen.speed(0)
        pen.hideturtle()
        button = turtle.Turtle()
        button.hideturtle()
        button.shape('square')
        button.fillcolor('Black')
        button.penup()
        button.goto(150,-200)
        button.write("Stick", align='center', font=FONT)
        button.sety(-200+ CURSOR_SIZE + FONT_SIZE)
        button.onclick(self.player_stick)
        
        button.showturtle()
        print("999")
        
        pen = turtle.Turtle()
        pen.speed(0)
        pen.hideturtle()
        label = turtle.Turtle()
        label.hideturtle()
#label.shape('square')
#label.fillcolor('Black')
        label.penup()
        label.goto(-50,-100)
        label.write("Players cards", align='center', font=FONT)
        label.sety(-200+ CURSOR_SIZE + FONT_SIZE)
        label.showturtle()
        pen.hideturtle()

        pen = turtle.Turtle()
        pen.speed(0)
        pen.hideturtle()
        label = turtle.Turtle()
        label.hideturtle()
#label.shape('square')
#label.fillcolor('Black')
        label.penup()
        label.goto(-50,280)
        label.write("Dealers cards", align='center', font=FONT)
        label.sety(-200+ CURSOR_SIZE + FONT_SIZE)
        label.showturtle()
        pen.hideturtle()


        balance = player.get_balance()
        b = Bank(player)
        b.get_balance()
        pen = turtle.Turtle()
        pen.speed(0)
        pen.hideturtle()
        label = turtle.Turtle()
        label.hideturtle()
#label.shape('square')
#label.fillcolor('Black')
        label.penup()
        label.goto(-200,-200)
        label.write(player.get_balance(), align='center', font=FONT)
        label.sety(-200+ CURSOR_SIZE + FONT_SIZE)
        label.showturtle()
        pen.hideturtle()
        #self.wn.mainloop()
         #playing = True
        self.player_score_num = 0
        #while playing:
        #self.deck = Deck()
        self.deck.shuffle()
        #self.score = Score()
        #self.player_score = Score()
        #self.dealer_score = Score()

        #for i in range(2):
        self.player_score.player_add_card(self.deck.get_card())
        print(self.player_score.player_add_card(self.deck.get_card()))
        #self.deck = Deck()
        self.dealer_score.dealer_add_card(self.deck.get_card())
        print(self.dealer_score.dealer_add_card(self.deck.get_card()))
        self.dealer_score.display_dealer()
        self.player_score.display_player()
        print("jjjx")
        #print(self.player_score.display_player())
        #self.player_score.player_add_card(card)
        #self.player_cards.append(self.player_score.player_add_card(self.deck.get_card()))
        self.get_player_score(player_score)
        print("!!!!")
        self.set_player_score(player_score)
        print(self.player_score_num)
        
        
        print(self.player_score_num)
        print("hh")
        self.get_player_score(player_score)
       
        self.get_dealer_score(dealer_score)
        print("!!!!xxx")
        self.set_dealer_score(dealer_score)
        print(self.dealer_score_num)
        
        
        print(self.dealer_score_num)
        print("hhad")
        self.get_dealer_score(dealer_score)

        
        
        
        
        wn.mainloop()
    #def player_twist(self, x, y):

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
   
    def player_twist(self, x, y):
        go = Game_over()
        #self.deck = Deck()
        print("43434343433")
        #self.player_score.display_player()        
        print(self.player_score)
        #self.set_player_score(player_score)
        print(self.player_score_num)
        print("fgfgfgf")
        #self.player_score.get_value()
        print(self.player_score_num)
        #player_score = self.get_player_score_num(player_score_next_card)
        #self.deck = Deck()
        #self.deck.shuffle()
        #self.score = Score()
        #self.player_score = player_score
        #self.player_score = self.get_player_score(player_score)
        self.player_score.player_add_card(self.deck.get_card())
        print("333aax")
        self.score = Score()
        self.deck = Deck()
        self.player_score.get_value()
        print("333aa")
        print(self.player_score_num)
        self.player_score.display_player()
        #self.player_score.display_player_twist(x,y, player_score)
        #print(self.player_score.get_value())
        
        print("333")
        #player_score_next_card= self.player_score.get_value()
        #self.set_player_score(player_score)
        #self.player_score = self.player_score_num + player_score_next_card
        #self.player_score_num = self.player_score_num + self.player_score.get_value()
        #player_score = self.get_player_score_num( player_score_next_card)
        self.set_player_score(player_score)
        print("bbb")
        print(self.player_score_num)
        #self.is_over_21(player_score)
        if self.player_score_num  > 21:
          print("bust")
          go.play_again_lost()
  
    #def is_over_21(self, player_score):
     # self.get_player_score()
      #return self.player_score_num
     #player_score_next_card= self.player_score.get_value()
     #player_score_next_card= self.player_score
     #player_score_num = self.get_player_score_num(player_score_next_card) + self.player_score_num # this gets and sets self.player_score_num
     
     #if self.player_score_num < 21:
        #self.get_player_score_num(player_score_num, player_score_next_card)
      #  print("222")
        #print(player_score_num)
        
       # print(player_score_next_card)
        #self.set_player_score_num(player_score_next_card, player_score_num)
        #self.player_score_num = self.player_score_num
        #self.player_score_num = self.set_player_score_num() + self.player_score_num
        #player_score_num = self.set_player_score_num(player_score_num) + player_score_num 
        #print("111")
        #self.set_player_score_num(player_score_next_card, player_score_num)
        #self.set_player_score_num(player_score_next_card, player_score_num)
        #print("zzz")
        #print(self.player_score_num)
        #player_score_num1 = player_score_num + player_score_num1
        #self.player_score_num = self.get_player_score_num(player_score_num, player_score_next_card) + self.player_score_num
        #self.get_player_score_num(player_score_num, player_score_next_card) # this gets and sets self.player_score_num

        #print(".....")
        #print(self.player_score_num)
        #print(self.player_score_num)
        #self.set_player_score_num()
        #self.player_score_num = int(player_score)
        #if self.player_score_num > 21:
         # print("BUST")
        #self.get_player_score()
        #return self.player_score_num
    """
    def set_player_score_num(self, player_score_next_card):
    #def set_player_score_num(self): 
      #while self.player_score_num < 21:
        print("7777")
        print(self.player_score_num)
        player_hand = self.player_score_num + player_score_next_card 
      
        print(self.player_score_num)
        print("eeee")
        print(player_score_next_card)
        self.player_score_num = self.player_score_num + player_score_next_card
        print("yyy")
        print(self.player_score_num)
        print("nnn")
        print(self.player_score_num)
        print(player_hand)
        #return player_score_num
        self.player_score_num = player_hand 
    
    def get_player_score_num(self,player_score_next_card):
        #player_score_num = self.player_score_num
        print("888")
        self.set_player_score_num(player_score_next_card)
        return self.player_score_num
    
"""    
    def player_stick(self, x, y):
        self.dealer_score.display_dealer_stick()
        go = Game_over()
        self.score = Score()
        self.deck = Deck()
        print("eee")
        self.dealer_score.get_value_dealer()
        #self.set_dealer_score(dealer_score)
        #self.set_player_score(player_score)
        print(self.player_score_num)    
        print(self.dealer_score_num)
        print("123456789")
        print(self.player_score_num)
        while self.dealer_score_num < 17 and self.player_score_num >= self.dealer_score_num:
         self.dealer_score.dealer_add_card(self.deck.get_card()) 
         self.dealer_score.display_dealer_stick()
         self.dealer_score_num = self.dealer_score.get_value_dealer()
        if self.dealer_score_num > 21:
          print("dealer bust player wins")
          go.play_again_win()
        elif self.player_score_num > self.dealer_score_num:
          print("Player wins")
          go.play_again_win()
        elif self.player_score_num < self.dealer_score_num:

          print("Dealer wins")
          go.play_again_lost()
        else:
            go.play_again_draw()


class Game_over:
  def __init__(self):
    pass   

  def play_again_win(self):
      pen = turtle.Turtle()
      pen.color("green")
      pen.speed(0)
      pen.hideturtle()
      pen.hideturtle()
      pen.begin_fill()
#pen.forward(-250)
      pen.forward(550)
      pen.left(90) 
      pen.forward(300)
      pen.left(90)
      pen.forward(800)
      pen.left(90) 
      pen.forward(800)
      pen.left(90)
      pen.forward(800)
      pen.left(90)
      pen.forward(1000)
      pen.end_fill()
      g = Game(player_score, dealer_score, player_score_num)
      print("game over")
      CURSOR_SIZE = 20
      FONT_SIZE = 12
      FONT = ('Arial', FONT_SIZE, 'bold')
      pen = turtle.Turtle()
      pen.speed(0)
      pen.hideturtle()
      button = turtle.Turtle()
      button.hideturtle()
      button.shape('square')
      button.fillcolor('red')
      button.penup()
      button.goto(000, -50)
      button.write("Play again", align='center', font=FONT)
      button.sety(-50+ CURSOR_SIZE + FONT_SIZE)  
      g = Game(player_score, dealer_score, player_score_num)
      button.onclick(g.play)
      button.showturtle()
      button = turtle.Turtle()
      button.hideturtle()
      button.shape('square')
      button.fillcolor('black')
      button.penup()
      button.goto(-100, -50)
      button.write("Quit", align='center', font=FONT)
      button.sety(-50+ CURSOR_SIZE + FONT_SIZE)  
      button.onclick(self.quit)
      button.showturtle() 
      FONT_SIZE = 50
      FONT = ('Arial', FONT_SIZE, 'bold')
      pen.hideturtle()
      pen.begin_fill()
      pen.forward(-250)
      pen.forward(400)
      pen.left(90) 
      pen.forward(100)
      pen.left(90)
      pen.forward(400)
      pen.left(90) 
      pen.forward(100)
      pen.left(90)
      pen.end_fill()
      pen.hideturtle()
#pen.color("red")
      pen.goto(-50, 20)
      pen.color("red")
      pen.write("You win", align='center', font=FONT)
      Game(player_score, dealer_score, player_score_num)




  def play_again_lost(self):
      pen = turtle.Turtle()
      pen.color("green")
      pen.speed(0)
      pen.hideturtle()
      pen.hideturtle()
      pen.begin_fill()
#pen.forward(-250)
      pen.forward(550)
      pen.left(90) 
      pen.forward(300)
      pen.left(90)
      pen.forward(800)
      pen.left(90) 
      pen.forward(800)
      pen.left(90)
      pen.forward(800)
      pen.left(90)
      pen.forward(1000)
      pen.end_fill()
      g = Game(player_score, dealer_score, player_score_num)
      print("game over")
      CURSOR_SIZE = 20
      FONT_SIZE = 12
      FONT = ('Arial', FONT_SIZE, 'bold')
      pen = turtle.Turtle()
      pen.speed(0)
      pen.hideturtle()
      button = turtle.Turtle()
      button.hideturtle()
      button.shape('square')
      button.fillcolor('red')
      button.penup()
      button.goto(000, -50)
      button.write("Play again", align='center', font=FONT)
      button.sety(-50+ CURSOR_SIZE + FONT_SIZE)  
      g = Game(player_score, dealer_score, player_score_num)
      button.onclick(g.play)
      button.showturtle()
      button = turtle.Turtle()
      button.hideturtle()
      button.shape('square')
      button.fillcolor('black')
      button.penup()
      button.goto(-100, -50)
      button.write("Quit", align='center', font=FONT)
      button.sety(-50+ CURSOR_SIZE + FONT_SIZE)  
      button.onclick(self.quit)
      button.showturtle() 
      FONT_SIZE = 50
      FONT = ('Arial', FONT_SIZE, 'bold')
      pen.hideturtle()
      pen.begin_fill()
      pen.forward(-250)
      pen.forward(400)
      pen.left(90) 
      pen.forward(100)
      pen.left(90)
      pen.forward(400)
      pen.left(90) 
      pen.forward(100)
      pen.left(90)
      pen.end_fill()
      pen.hideturtle()
#pen.color("red")
      pen.goto(-50, 20)
      pen.color("red")
      pen.write("You lost", align='center', font=FONT)
      Game(player_score, dealer_score, player_score_num)

  def quit(self, x, y):
        #sys.exit()
        quit()


  def play_again_draw(self):
      pen = turtle.Turtle()
      pen.color("green")
      pen.speed(0)
      pen.hideturtle()
      pen.hideturtle()
      pen.begin_fill()
#pen.forward(-250)
      pen.forward(550)
      pen.left(90) 
      pen.forward(300)
      pen.left(90)
      pen.forward(800)
      pen.left(90) 
      pen.forward(800)
      pen.left(90)
      pen.forward(800)
      pen.left(90)
      pen.forward(1000)
      pen.end_fill()
      g = Game(player_score, dealer_score, player_score_num)
      print("game over")
      CURSOR_SIZE = 20
      FONT_SIZE = 12
      FONT = ('Arial', FONT_SIZE, 'bold')
      pen = turtle.Turtle()
      pen.speed(0)
      pen.hideturtle()
      button = turtle.Turtle()
      button.hideturtle()
      button.shape('square')
      button.fillcolor('red')
      button.penup()
      button.goto(000, -50)
      button.write("Play again", align='center', font=FONT)
      button.sety(-50+ CURSOR_SIZE + FONT_SIZE)  
      g = Game(player_score, dealer_score, player_score_num)
      button.onclick(g.play)
      button.showturtle()
      button = turtle.Turtle()
      button.hideturtle()
      button.shape('square')
      button.fillcolor('black')
      button.penup()
      button.goto(-100, -50)
      button.write("Quit", align='center', font=FONT)
      button.sety(-50+ CURSOR_SIZE + FONT_SIZE)  
      button.onclick(self.quit)
      button.showturtle() 
      FONT_SIZE = 50
      FONT = ('Arial', FONT_SIZE, 'bold')
      pen.hideturtle()
      pen.begin_fill()
      pen.forward(-250)
      pen.forward(400)
      pen.left(90) 
      pen.forward(100)
      pen.left(90)
      pen.forward(400)
      pen.left(90) 
      pen.forward(100)
      pen.left(90)
      pen.end_fill()
      pen.hideturtle()
#pen.color("red")
      pen.goto(-50, 20)
      pen.color("red")
      pen.write("Draw", align='center', font=FONT)
      Game(player_score, dealer_score, player_score_num)




























  def play_again_win_blackjack(self):
      pen = turtle.Turtle()
      pen.color("green")
      pen.speed(0)
      pen.hideturtle()
      pen.hideturtle()
      pen.begin_fill()
#pen.forward(-250)
      pen.forward(550)
      pen.left(90) 
      pen.forward(300)
      pen.left(90)
      pen.forward(800)
      pen.left(90) 
      pen.forward(800)
      pen.left(90)
      pen.forward(800)
      pen.left(90)
      pen.forward(1000)
      pen.end_fill()
      g = Game(player_score, dealer_score, player_score_num)
      print("game over")
      CURSOR_SIZE = 20
      FONT_SIZE = 12
      FONT = ('Arial', FONT_SIZE, 'bold')
      pen = turtle.Turtle()
      pen.speed(0)
      pen.hideturtle()
      button = turtle.Turtle()
      button.hideturtle()
      button.shape('square')
      button.fillcolor('red')
      button.penup()
      button.goto(000, -50)
      button.write("Play again", align='center', font=FONT)
      button.sety(-50+ CURSOR_SIZE + FONT_SIZE)  
      g = Game(player_score, dealer_score, player_score_num)
      button.onclick(g.play)
      button.showturtle()
      button = turtle.Turtle()
      button.hideturtle()
      button.shape('square')
      button.fillcolor('black')
      button.penup()
      button.goto(-100, -50)
      button.write("Quit", align='center', font=FONT)
      button.sety(-50+ CURSOR_SIZE + FONT_SIZE)  
      button.onclick(self.quit)
      button.showturtle() 
      FONT_SIZE = 10
      FONT = ('Arial', FONT_SIZE, 'bold')
      pen.hideturtle()
      pen.begin_fill()
      pen.forward(-250)
      pen.forward(400)
      pen.left(90) 
      pen.forward(100)
      pen.left(90)
      pen.forward(400)
      pen.left(90) 
      pen.forward(100)
      pen.left(90)
      pen.end_fill()
      pen.hideturtle()
#pen.color("red")
      pen.goto(-50, 20)
      pen.color("red")
      pen.write("You win you got a black jack", align='center', font=FONT)
      Game(player_score, dealer_score, player_score_num)


  def play_again_lost_blackjack(self):
      pen = turtle.Turtle()
      pen.color("green")
      pen.speed(0)
      pen.hideturtle()
      pen.hideturtle()
      pen.begin_fill()
#pen.forward(-250)
      pen.forward(550)
      pen.left(90) 
      pen.forward(300)
      pen.left(90)
      pen.forward(800)
      pen.left(90) 
      pen.forward(800)
      pen.left(90)
      pen.forward(800)
      pen.left(90)
      pen.forward(1000)
      pen.end_fill()
      g = Game(player_score, dealer_score, player_score_num)
      print("game over")
      CURSOR_SIZE = 20
      FONT_SIZE = 12
      FONT = ('Arial', FONT_SIZE, 'bold')
      pen = turtle.Turtle()
      pen.speed(0)
      pen.hideturtle()
      button = turtle.Turtle()
      button.hideturtle()
      button.shape('square')
      button.fillcolor('red')
      button.penup()
      button.goto(000, -50)
      button.write("Play again", align='center', font=FONT)
      button.sety(-50+ CURSOR_SIZE + FONT_SIZE)  
      g = Game(player_score, dealer_score, player_score_num)
      button.onclick(g.play)
      button.showturtle()
      button = turtle.Turtle()
      button.hideturtle()
      button.shape('square')
      button.fillcolor('black')
      button.penup()
      button.goto(-100, -50)
      button.write("Quit", align='center', font=FONT)
      button.sety(-50+ CURSOR_SIZE + FONT_SIZE)  
      button.onclick(self.quit)
      button.showturtle() 
      FONT_SIZE = 10
      FONT = ('Arial', FONT_SIZE, 'bold')
      pen.hideturtle()
      pen.begin_fill()
      pen.forward(-250)
      pen.forward(400)
      pen.left(90) 
      pen.forward(100)
      pen.left(90)
      pen.forward(400)
      pen.left(90) 
      pen.forward(100)
      pen.left(90)
      pen.end_fill()
      pen.hideturtle()
#pen.color("red")
      pen.goto(-50, 20)
      pen.color("red")
      pen.write("You lost the dealer got a black jack", align='center', font=FONT)
      Game(player_score, dealer_score, player_score_num)







"""        
# Create deck                
deck = Deck()

# Shuffle deck
deck.reset()

# Render 2 cards (back) in a row
start_x = -100
for x in range(2):
    card = Card("", "")
    card.render(start_x + x * 125, 200, pen)

time.sleep(1)

# Render 2 cards in a row
start_x = -100
for x in range(2):
    card = deck.get_card()
    card.render(start_x + x * 125, 200, pen)
"""
"""
start_x = -100
for x in range(2):
    card = Card("", "")
    card.render(start_x + x * 125, 0, pen)

time.sleep(1)

# Render 2 cards in a row
start_x = -100
for x in range(2):
    card = deck.get_card()
    card.render(start_x + x * 125, 0, pen)
"""

"""
    start_x = -200
    for x in range(2):
        card = Card("", "")
        card.render(start_x + x * 125, 0, pen)

    time.sleep(1)

# Render 2 cards in a row
    start_x = -200
    for x in range(2):
        card = deck.get_card()
        card.render(start_x + x * 125, 0, pen)

"""

class Bank:
    def __init__(self, balance):
        self.balance = balance

    def set_balance(self, balance):
        self.balance = balance


    def get_balance(self):
            return self.balance
            print(balance)
    

    def set_new_balance(self, new_balance):
        player.set_balance(new_balance)
        #print(new_balance)

player = Bank(1000)
    





if __name__ == "__main__":
    x = 0
    y = 0
    player_score_num = 0
    g = Game(player_score, dealer_score, player_score_num)
    g.play(x, y)

#wn.mainloop()

# i need to write a deal function which alos prints the cards.
