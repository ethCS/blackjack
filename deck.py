######################
# deck.py
# ethan elliott
# csci151
# 4/29/25
######################

import stdio
import random
from card import Card

#this is the deck class that holds the deck of cards
#it takes in the suit, face, and value of the card
#it has methods to create a new deck, shuffle the deck, deal a card, and get the size of the deck
#it also has a method to print the deck
class Deck:
    """
    A class representing a standard playing card deck.
    
    This class creates and manages a standard 52-card deck with the ability to
    shuffle cards, deal cards, and keep track of the remaining cards in the deck.
    
    Attributes:
        _deck (list): A list containing Card objects representing the deck of cards
    """
    
    def __init__(self):
        """
        Initialize a new Deck object.
        
        Creates a new deck of 52 cards and shuffles it upon initialization.
        """
        self._deck = []
        self._new_deck()
        self._shuffle_deck()
    
    def _new_deck(self):
        """
        Creates a new standard 52-card deck.
        
        Populates the deck with 13 cards (Ace through King) for each of the 
        four suits (Spades, Clubs, Diamonds, Hearts).
        
        Note: There appears to be a naming inconsistency between this method and
        the method called in __init__ (_new_deck).
        """
        for s in ["Spades", "Clubs", "Diamonds", "Hearts"]:
            self._deck.append(Card(s, "Ace", 1))
            self._deck.append(Card(s, "Two", 2))
            self._deck.append(Card(s, "Three", 3))
            self._deck.append(Card(s, "Four", 4))
            self._deck.append(Card(s, "Five", 5))
            self._deck.append(Card(s, "Six", 6))
            self._deck.append(Card(s, "Seven", 7))
            self._deck.append(Card(s, "Eight", 8))
            self._deck.append(Card(s, "Nine", 9))
            self._deck.append(Card(s, "Ten", 10))
            self._deck.append(Card(s, "Jack", 10))
            self._deck.append(Card(s, "Queen", 10))
            self._deck.append(Card(s, "King", 10))
    
    def print_deck(self):
        """
        Prints all cards in the current deck.
        
        Each card is printed on a new line using the card's string representation.
        """
        for c in self._deck:
            stdio.writeln(c)
    
    def _shuffle_deck(self):
        """
        Shuffles the deck randomly.
        
        Uses the random.shuffle function to randomize the order of cards in the deck.
        
        Note: There appears to be a naming inconsistency between this method and
        the method called in __init__ (_shuffle_deck).
        """
        random.shuffle(self._deck)
    
    def deal(self):
        """
        Deals a card from the top of the deck.
        
        Returns:
            Card: The top card from the deck.
            
        Note: This method removes the card from the deck.
        """
        return self._deck.pop(0)
    
    def deck_size(self):
        """
        Returns the current number of cards in the deck.
        
        Returns:
            int: The number of cards remaining in the deck.
        """
        return len(self._deck)
   
def main():
    """
    Main function to demonstrate the Deck class functionality.
    
    Creates a new deck, prints all cards, deals one card, and displays
    the number of cards remaining in the deck.
    """
    d1 = Deck()
    d1.print_deck()
    stdio.writeln()
    stdio.writeln("Deal card: ")
    c = d1.deal()
    stdio.writeln(c)
    stdio.writeln("Number of cards in deck : ")
    stdio.writeln(d1.deck_size())

if __name__ == "__main__":
    main()