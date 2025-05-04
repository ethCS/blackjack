######################
#card.py
#ethan elliott
#csci151
#4/29/25
######################
import stdio

#this is the card class that holds the card object
#it takes in the suit, face, and value of the card
#it has methods to get the value, face, and set the value of the card
class Card:
    '''
    A class to represent a card.
    Attributes
    ----------------
    _suit: str
        suit of card
    _face : str
        face of card
    _value : int
        value of card
    Methods
    ----------------
    get_value()
        returns the value of card
    get_face()
        returns the face of card
    set_value(x)
        Sets the value of card to x
    __str__()
        returns string representation of the card
    '''
    def __init__(self, suit, face, value):
        '''
        Constructs all the necessary attributes for the card object.
        Parameters
        -------------
        suit : str
            The suit of the card (Hearts, Diamonds, Clubs, Spades)
        face : str
            The face value of the card (Two, Three, ..., King, Ace)
        value : int
            The numerical value of the card
        '''
        self._suit = suit
        self._face = face
        self._value = value
    def get_value(self):
        '''
        Returns the numerical value of the card.
        Returns
        -------------
        int
            The value of the card
        '''
        return self._value
   
    def get_face(self):
        '''
        Returns the face of the card.
        Returns
        -------------
        str
            The face of the card
        '''
        return self._face
    def set_value(self, v):
        '''
        Sets the numerical value of the card.
        Parameters
        -------------
        v : int
            The new value to assign to the card
        Returns
        -------------
        None
        '''
        self._value = v
        return
    def __str__(self):
        '''
        Returns a string representation of the card.
        Returns
        -------------
        str
            A string in the format "face of suit"
        '''
        return ('{} of {}'.format(self._face, self._suit))
    
#this is the main function that creates two card objects
#and displays them
#it also demonstrates getting and setting the value of a card
def main():
    '''
    Main function to demonstrate the usage of the Card class.
    Creates two card objects, displays them, and demonstrates
    getting and setting card values.
    '''
    c1 = Card("Hearts", "Two", 2)
    c2 = Card("Clubs", "Ace", 1)
    stdio.writeln("First card:")
    stdio.writeln(c1)
    stdio.writeln("Second card:")
    stdio.writeln(c2)
    stdio.writeln()
    stdio.writeln("Getting value of second card")
    stdio.writeln(c2.get_value())
    c2.set_value(11)
    stdio.writeln("Getting value of second card after setting to 11")
    stdio.writeln(c2.get_value())
if __name__ == "__main__":
    main()