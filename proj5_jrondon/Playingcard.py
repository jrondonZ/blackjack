# Christopher, Josiah, Ava
#Playing card class, 11.19.2022

import random

#This class makes the playingcards 
#rank and suit are numbers and letters
#Allows cards to be displayed in the same fashion as the images associated with each card
class Card:
    def __init__(self,suit,rank):
        self.suit = suit
        self.rank = rank
    #rank and suit are numbers and letters
    #Allows cards to be displayed in the same fashion as the images associated with each card
    
    #returns the suit for card
    def getSuit(self):
        return self.suit
    
    #returns the rank for card  
    def getRank(self):
        return self.rank 

    #cards with values of 10+ such as king,queen, and jack
    #we figured it'd be best to leave str function out for better functionality for the blackjackgame itself
    def value(self):
        if self.rank > 10:
            return 10 
        else:
            return int(self.rank)#numerical cards(2,3,4,5...)
            
    #  def __str__(self):
    #  return self.getSuit() + self.getRank()