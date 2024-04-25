# Josiah Rondon
#11/29/22
#File: Deck.py
#Deck class

from Playingcard import *

#Deck class is defined, and inside the methods shuffle and draw are created.
#In this class it creates the playing deck of cards, and re-labels the cards so that they match up with the images.
#Additionally, the two created methods allow for more features when playing the game.
class Deck:
    def __init__(self):
        #Empty list is created.
        self.decklist = []
        
        #All of the potential suits are stored in a list.
        SuitList = ['s', 'c', 'h', 'd']

        #The cards are now being labelled as their corresponding image is titled.
        for r in range(13):
            for s in range(4):
                card = Card(SuitList[s], r+1)
                self.decklist.append(card)
    
    #Shuffles the cards in the deck.
    def shuffle(self):
        random.shuffle(self.decklist)
        pass

    #Lets the user draw a card, and additionally shows them the card itself.
    def drawCard(self):
        topCard = self.decklist[0]
        self.decklist.remove(topCard)
        return topCard
