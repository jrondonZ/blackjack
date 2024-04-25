#Christopher, Josiah, Ava
#Black Jack game with graphics, 11.19.2022

from graphics import *
from random import *
from ButtonClass import *
from Deck import *
from Playingcard import *

#this class runs the blackjack game, using the imported modules 
class Blackjack:
     # deck gets shuffled here, the two hands that'll later be changed
    def __init__(self):

        self.Dhand = []
        self.deck = Deck()
        self.PHand = []
        self.deck.shuffle()
    
    def initDeal(self, win, x1, y1, x2, y2, Plist, Dlist):
        for i in range(2):
            CardP = self.deck.drawCard()
            self.PHand.append(CardP)
            #A card is drawn and added to the player's hand
            ImageP=Image(Point(x1+100*i, y1), "playingcards/"+str(CardP.getSuit())+str(CardP.getRank())+".gif")
            ImageP.draw(win)
            #The images of the respective cards get drawn at a constant distance from each other
            #The rank and suit are directly tied to the image names, i.e., Ace of Spades is s1
            Plist.append(ImageP)
            #This is to make a list of images drawn, which is relevant for undrawing them (more on this later)
        
        #first dealer card assessed here, revealed will be drawn later 
        CardD1=self.deck.drawCard()
        CardD2=self.deck.drawCard()
        self.Dhand.append(CardD1)
        self.Dhand.append(CardD2)
        ImageD1=Image(Point(x2, y2), "playingcards/b1fv.gif")
        ImageD2=Image(Point(x2+100, y2), "playingcards/"+str(CardD2.getSuit())+str(CardD2.getRank())+".gif")
        ImageD1.draw(win)
        ImageD2.draw(win)
        Dlist.append(ImageD2)
       
        #gets the player hand
    def getHandP(self):
        return self.PHand
        #gets the dealer hand 
    def getHandD(self):
        return self.Dhand
        #this function draws new card and added to a list which is then undrawen
    def hit(self, win, x, y, Plist):
        NewCard=self.deck.drawCard()
        self.PHand.append(NewCard)
        card = Image(Point(x,y), "playingcards/"+str(NewCard.getSuit())+str(NewCard.getRank())+".gif")
        Plist.append(card)
        card.draw(win)

        #function made to evaluate a hand when hitting or standing(especially for dealer)
    def evalHand(self, hand):
        valueList = []
        #evaluating for aces 
        for i in range(len(hand)):
            valueList.append((hand[i].value()))
            
        val = 0
        #Aces are by default 1
        #Adds ten when given an ace to not go over 21
        for i in range(len(hand)):
            addition=hand[i].value()
            val = val + addition
            if val <= 11 and 1 in valueList:
                val = val + 10
            
        if val > 21 and 1 in valueList:
            val = val-10
                    
        return val
        #val needs to be directly accessed  

    def DealerPlays(self, win, x, y, Dlist):
        counter = 0
        #cards get spaced from each other 
        while self.evalHand(self.getHandD())<17:
            NewCardD = self.deck.drawCard()
            self.Dhand.append(NewCardD)
            card = Image(Point(x+100*counter,y), "playingcards/"+str(NewCardD.getSuit())+str(NewCardD.getRank())+".gif")
            card.draw(win)
            Dlist.append(card)
            #Draws the card from the deck, makes image, stores the image
            counter = counter + 1
            #Updating counter 
        Reveal=Image(Point(250, 100), "playingcards/"+str(self.getHandD()[0].getSuit())+str(self.getHandD()[0].getRank())+".gif")
        Reveal.draw(win)
        Dlist.append(Reveal)
        #unrevealed card gets revealed, and then stored to be undrawn
        
#handy function a friend showed me
def TextPlacer(win, x, y, label):
    text=Text(Point(x,y), label)
    text.setSize(20)
    text.draw(win)
    return text

def main():
    #calls blackjack class
    play=Blackjack()
    
    win = GraphWin("blackjack", 600, 600)
    win.setBackground('darkgreen')
    #makes window at set x,y coordinates
    
    #border is made using line method,setWidth,setFill etc..
    border1 = Line(Point(0,5), Point(600,5))
    border2 = Line(Point(5,5), Point(5, 600))
    border3 = Line(Point(595,5), Point(595,600))
    border4 = Line(Point(595,595), Point(0,595))
    
    border1.setWidth(50)
    border1.setFill('saddlebrown')
    border1.draw(win)
    border2.setWidth(50)
    border2.setFill('saddlebrown')
    border2.draw(win)
    border3.setWidth(50)
    border3.setFill('saddlebrown')
    border3.draw(win)
    border4.setWidth(50)
    border4.setFill('saddlebrown')
    border4.draw(win)
    
    #Intro message prompting user to start blackjack
    line1 = TextPlacer(win, 600, 200, "Welcome")
    line2 = TextPlacer(win, 0, 250, "To")
    line3 = TextPlacer(win, 600,300, "Blackjack!")

    line1.setSize(30)
    line1.setFill('black')
    line1.setStyle('bold')
    line2.setSize(30)
    line2.setFill('black')
    line2.setStyle('bold')
    line3.setSize(30)
    line3.setFill('black')
    line3.setStyle('bold')

    for i in range(30):
        line1.move(-10,0)
        line2.move(10,0)
        line3.move(-10,0)

    introMess = TextPlacer(win, 300,400, 'Click anywhere to continue!')

    win.getMouse()

    line1.undraw()
    line2.undraw()
    line3.undraw()
    introMess.undraw()

    InstHeading = TextPlacer(win, 300, 100, 'Directions for Blackjack')
    InstHeading.setSize(40)
    InstHeading.setStyle('bold')
    Inst1 = TextPlacer(win, 150, 200, '• Press HIT to draw a card')
    Inst2 = TextPlacer(win, 185, 250, '• Press STAND if you would like to')
    Instr2 = TextPlacer(win, 185, 275, 'stay at your current card amount')
    Inst3 = TextPlacer(win, 200, 325, '• If any player is over 21, YOU BUST ')
    Inst4 = TextPlacer(win, 150, 370, '• Here are the card Values')
    cardVal = TextPlacer(win, 225, 400, '- Number cards are the same as card value')
    faceVal = TextPlacer(win, 180, 425, '- Face Cards = 10, Ace = 1 or 11')
    contLabel = TextPlacer(win, 300, 500, 'Click anywhere to continue!')

    win.getMouse()

    InstHeading.undraw()
    Inst1.undraw()
    Inst2.undraw()
    Instr2.undraw()
    Inst3.undraw()
    Inst4.undraw()
    cardVal.undraw()
    faceVal.undraw()
    contLabel.undraw()

    # 4 buttons here using the Button class, each with respective purpose
    HitBTN = Button(win, Point(200,300), 100, 50,"Hit")
    StandBTN = Button(win, Point(400,300), 100, 50, "Stand")
    QuitBTN = Button(win, Point(75, 550), 60, 30, "Quit")
    NewGameBTN= Button(win, Point(525, 550), 60, 30, "New Game")

    #2 lists for storing images
    Plist = []
    Dlist = []
    
    #blackjack class is now assessed in window along with the 2 lists made for each hand
    play.initDeal(win, 200, 425, 250, 100, Plist, Dlist)
    ValueP = TextPlacer(win, 125, 355, "Your hand: \n"+str(play.evalHand(play.getHandP())))
    ValueD = TextPlacer(win, 125, 75, "Dealer's hand: \n?")

    Prompt=TextPlacer(win, 200, 100, "")
    # "New Game" can be clicked, even not playing blackjack
    
    target=win.getMouse()
    while not QuitBTN.clicked(target):
        
        #the game is assessed while quit button isn't clicked
        
        if HitBTN.clicked(target):
            play.hit(win, 200+100*len(play.getHandP()), 425, Plist)
            #new cards at a distance from the initial proportion 
            #to ensure that they won't get drawn on top of each other
            ValueP.undraw()
            ValueP=TextPlacer(win, 125, 355, "Your hand: \n"+str(play.evalHand(play.getHandP())))
            #displays the new hand value
            if play.evalHand(play.getHandP())>21:
                Prompt.undraw()
                Prompt=TextPlacer(win, 300, 250, "You busted! Dealer wins.")
                #Text displayed when players hand exceeds 21, game over
                
        if StandBTN.clicked(target):
            play.DealerPlays(win, 350, 125, Dlist)
            ValueD.undraw()
            ValueD=TextPlacer(win, 125, 75, "Dealer's hand: \n"+str(play.evalHand(play.getHandD())))
            #Displays dealer's hand value 

            #Using the same definition for each scenario below. Will be referred to when undrawen
            if play.evalHand(play.getHandD())>21:
                Prompt.undraw()
                Prompt=TextPlacer(win, 300, 250, "Dealer busted! You win.")
            elif play.evalHand(play.getHandD())==play.evalHand(play.getHandP()):
                Prompt.undraw()
                Prompt=TextPlacer(win, 400, 600, "Draw.")
            elif play.evalHand(play.getHandD())>play.evalHand(play.getHandP()):
                Prompt.undraw()
                Prompt=TextPlacer(win, 300, 250, "Dealer wins!")
            else:
                Prompt.undraw()
                Prompt=TextPlacer(win, 300, 250, "You win!")
        #this functions creates a new game when clicked
        
        if NewGameBTN.clicked(target):
            #Prompt get undrawen
            Prompt.undraw()
            
            #removing cards from player's hand and back into deck
            while len(play.getHandP())>0:
                
                Card=play.getHandP()[-1]
                play.deck.decklist.append(Card)
                play.PHand.remove(Card)
            
            #removing cards from dealer's hand and back into deck
            while len(play.getHandD())>0:
                Card=play.getHandD()[-1]
                play.deck.decklist.append(Card)
                play.Dhand.remove(Card)
            
            #undrawevery card image up to this point to place new ones in same location
            for i in range(len(Plist)):
                Plist[i].undraw()
            for i in range(len(Dlist)):
                Dlist[i].undraw()
            #Resetting the lists allows the process to be repeated over and 
            Dlist=[]
            #dealing again
            play.initDeal(win, 200, 425, 250, 100, Plist, Dlist)
            #undrawing the old displayed values
            ValueD.undraw()
            ValueD=TextPlacer(win, 125, 75, "Dealer's hand: \n?")
            ValueP.undraw()
            ValueP=TextPlacer(win, 124, 355, "Your hand: \n"+str(play.evalHand(play.getHandP())))
                
        target=win.getMouse()
        
    win.close()
    # "Quit" gets clicked and closes window  

if __name__ == "__main__":
    main()
