######################
#blackjack.py
#ethan elliott
#csci151
#4/29/25
######################

"""
Blackjack Game Implementation

This module implements a text-based Blackjack card game with the following rules:
- Standard Blackjack rules apply (aim for 21 without going over)
- Dealer stands on 17 or higher
- Natural Blackjack pays 3:2 (2.5x bet)
- Regular win pays 2x bet
- Tie results in bet returned (push)
- Deck is shuffled when fewer than 20 cards remain

Usage:
    Run this file directly to start a game:
    $ python blackjack.py

Dependencies:
    - stdio: Custom module for input/output operations
    - deck: Module containing the Deck class for card operations
    - player: Module containing the Player class for player management

Classes:
    No classes defined in this module. Game logic is implemented through functions.

Functions:
    game(): Handles a single round of blackjack
    main(): Entry point for the program, handles game setup and main loop
"""

import stdio

from deck import Deck
from player import Player

#this is the game function that holds the game logic
#it takes in the deck, player, dealer, player_deck, dealer_deck, and bet_amount
#and runs the game logic
#it handles the game flow, including dealing cards, player and dealer turns, and determining the winner
def game(deck, player, dealer, player_deck, dealer_deck, bet_amount):
    """
    Execute a single round of blackjack.

    This function handles the complete flow of a blackjack round including:
    - Initial card dealing
    - Player's turn (hit or stand decisions)
    - Dealer's turn (following house rules)
    - Determining the winner and updating balances

    Args:
        deck (Deck): The card deck to draw from
        player (Player): The human player object
        dealer (Player): The dealer (computer) player object
        player_deck (list): The player's current hand of cards
        dealer_deck (list): The dealer's current hand of cards
        bet_amount (int): The amount the player has bet on this round

    Returns:
        None
    """
    while True:
        dealer_deck.append(deck.deal())
        player_deck.append(deck.deal())
        player_deck.append(deck.deal())

        player.assign_deck(player_deck)
        dealer.assign_deck(dealer_deck)

        if deck.deck_size() < 20:
            deck._shuffle_deck()
            stdio.writeln("Deck Shuffled")

        stdio.writeln()
        stdio.writeln("****************")
        player.print_hand()
        stdio.writeln("****************")
        dealer.print_hand()
        stdio.writeln("****************")

        # player turn: hit or stand until 21, bust, or decision to stand
        natural_blackjack = False
        player_lost = False
        while True:
            if player.has_blackjack() == True:
                if len(player_deck) == 2:
                    natural_blackjack = True
                break
            if player.get_total_hand_count() > 21:
                stdio.writeln("You lose!")
                stdio.writeln("****************")
                dealer.print_hand()
                stdio.writeln("****************")
                player_lost = True
                break
            if player.get_total_hand_count() < 21:
                stdio.writeln("Hit? (y for yes)")
                hit_checker = stdio.readString()
                if hit_checker.lower() == "y":
                    player_deck.append(deck.deal())
                    player.assign_deck(player_deck)
                    stdio.writeln("****************")
                    player.print_hand()
                    stdio.writeln("****************")
                else:
                    break

        # Dealer turn: follows house rules
        # - Dealer must hit until 17 or higher
        # - Dealer wins ties except for natural blackjack ties
        dealer_deck.append(deck.deal())
        dealer.assign_deck(dealer_deck)

        if natural_blackjack and dealer.has_blackjack() == True:
            stdio.writeln("****************")
            dealer.print_hand()
            stdio.writeln("****************")
            stdio.writeln("Push / Tie")
            stdio.writeln("You get your bet back.")
            player.deposit(bet_amount)
            break
        if natural_blackjack and dealer.has_blackjack() == False:
            stdio.writeln("****************")
            dealer.print_hand()
            stdio.writeln("****************")
            stdio.writeln("You win with a natural blackjack!")
            player.deposit(bet_amount * 2.5)
            break

        while True and player_lost == False:
            if dealer.get_total_hand_count() > 21:
                stdio.writeln("****************")
                dealer.print_hand()
                stdio.writeln("****************")
                stdio.writeln("Dealer busted!")
                player.deposit(bet_amount * 2)
                break
            if dealer.get_total_hand_count() >= 17:
                if dealer.get_total_hand_count() > player.get_total_hand_count():
                    stdio.writeln("****************")
                    dealer.print_hand()
                    stdio.writeln("****************")
                    stdio.writeln("Dealer wins!")
                    player.print_balance()
                    break
                elif dealer.get_total_hand_count() < player.get_total_hand_count():
                    stdio.writeln("****************")
                    dealer.print_hand()
                    stdio.writeln("****************")
                    stdio.writeln("You win!")
                    player.deposit(bet_amount * 2)
                    break
                else:
                    stdio.writeln("****************")
                    dealer.print_hand()
                    stdio.writeln("****************")
                    stdio.writeln("Push / Tie")
                    stdio.writeln("You get your bet back.")
                    player.deposit(bet_amount)
                    break
            else:
                dealer_deck.append(deck.deal())
                dealer.assign_deck(dealer_deck)
        break

#for testing purposes/running the program
def main():
    """
    Main entry point for the Blackjack game.

    This function:
    - Prompts for player information (name and starting balance)
    - Handles betting
    - Creates game objects (deck, player, dealer)
    - Controls the main game loop, allowing multiple rounds of play
    - Manages end-game scenarios

    Returns:
        None
    """
    stdio.writeln("What is your name?")
    name = stdio.readString()
    stdio.writeln("How many dollars in chips would you like?")
    balance = stdio.readInt()
    stdio.writeln()
    stdio.writeln("------------")
    stdio.writeln(f"{name}'s balance: ${balance}")
    stdio.writeln("------------")
    stdio.writeln()

    deck = Deck()
    player = Player(name, balance)
    dealer = Player("Dealer", 0)
    player_deck = []
    dealer_deck = []

    while True:
        stdio.writeln("How much money would you like to bet? (specify num of dollars):")
        bet_amount = stdio.readInt()

        if (player.bet(bet_amount) == False):
            stdio.writeln("Would you like to play again? (y for yes/n for no)")
            continue_checker = stdio.readString()
            if continue_checker.lower() != "y":
                break
        else:
            stdio.writeln("****************")
            stdio.writeln("GOOD LUCK!!!")
            stdio.writeln("****************")
            game(deck, player, dealer, player_deck, dealer_deck, bet_amount)
            stdio.writeln("Would you like to play again? (y for yes/n for no)")
            continue_checker = stdio.readString()
            if continue_checker.lower() != "y":
                break
            player_deck = []
            dealer_deck = []
            player.clear()
            dealer.clear()
            stdio.writeln()
    stdio.writeln("Thanks for playing!")

#test client
if __name__ == "__main__":
    main()