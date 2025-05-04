######################
# player.py
# ethan elliott
# csci151
# 4/29/25
######################
import stdio

# this is the player class that holds the player object
# it takes in the name, hand, and balance of the player
# it has methods to print the hand, clear the hand, print the balance,
# bet, deposit, assign the deck, get the total hand count, and check if the player has blackjack
class Player:
    """
    Represents a player in a card game.
    
    This class manages a player's name, hand of cards, and balance.
    It provides functionality for betting, viewing cards, and managing currency.
    
    Attributes:
        _name (str): The player's name.
        _hand (list): The player's current hand of cards.
        _balance (float): The player's current monetary balance.
    """
    
    def __init__(self, name, balance):
        """
        Initialize a new Player object.
        
        Args:
            name (str): The player's name.
            balance (float): The player's starting balance.
        
        Returns:
            None
        """
        self._name = name
        self._hand = []
        self._balance = balance
        return
    
    def print_hand(self):
        """
        Display all cards in the player's hand.
        
        Prints the player's name followed by each card in their hand.
        
        Returns:
            None
        """
        stdio.writeln(self._name + "'s hand:\n")
        for c in self._hand:
            stdio.writeln(c)
        stdio.writeln()
        return
    
    def clear(self):
        """
        Remove all cards from the player's hand.
        
        Resets the player's hand to an empty list and notifies the user.
        
        Returns:
            None
        """
        self._hand = []
        stdio.writeln("Cleared hand.")
        return
    
    def print_balance(self):
        """
        Display the player's current balance.
        
        Prints the player's name and their current monetary balance.
        
        Returns:
            None
        """
        stdio.writeln(f"{self._name}'s current balance is: ${self._balance}")
    
    def bet(self, bet_amount):
        """
        Place a bet with the specified amount.
        
        Validates if the bet amount is valid (positive and within the player's balance)
        and deducts it from the player's balance if valid.
        
        Args:
            bet_amount (float): The amount to bet.
            
        Returns:
            bool: True if the bet was successful, False otherwise.
        """
        if bet_amount > self._balance:
            stdio.writeln(f"You do not have enough in your balance to bet that amount.")
            return False
        elif bet_amount < 0:
            stdio.writeln(f"Your bet amount cannot be less than zero.")
            return False
        else:
            self._balance -= bet_amount
        return True
    
    def deposit(self, value):
        """
        Add funds to the player's balance.
        
        Validates if the deposit amount is positive and adds it to the player's balance.
        
        Args:
            value (float): The amount to deposit.
            
        Returns:
            None
        """
        if value <= 0:
            stdio.writeln("needs to be positive...")
        else:
            self._balance += value
            stdio.writeln(f"Deposited ${value} to balance: ${self._balance}")
    
    def assign_deck(self, deck):
        """
        Set the player's hand to a specified deck of cards.
        
        Args:
            deck (list): A list of Card objects to assign as the player's hand.
            
        Returns:
            None
        """
        self._hand = deck
        return
    
    def get_total_hand_count(self):
        """
        Calculate the total value of the player's hand.
        
        Handles Ace cards with special logic, counting them as 11 unless that
        would cause the hand to exceed 21, in which case they count as 1.
        
        Returns:
            int: The total value of all cards in the player's hand.
        """
        total = 0
        ace_count = 0
        for i in self._hand:
            if i.get_face() == "Ace":
                ace_count += 1
            else:
                total += i.get_value()
        while ace_count != 0:
            if total + 11 > 21:
                total += 1
            else:
                total += 11
            ace_count -= 1
        return total
    
    def has_blackjack(self):
        """
        Check if the player has a blackjack (a hand with a value of 21).
        
        Returns:
            bool: True if the player has blackjack, False otherwise.
        """
        return self.get_total_hand_count() == 21


def main():
    """
    Test function demonstrating the Player class functionality.
    
    Creates a player instance and tests the betting functionality.
    
    Returns:
        None
    """
    p1 = Player("Ethan", 1999)
    stdio.writeln("\nTEST - Betting:")
    if not (p1.bet(600)):
        stdio.writeln("Betting $600, bet is more than balance: $600.")
    p1.print_balance()


if __name__ == "__main__":
    main()