# -*- coding: utf-8 -*-
"""
Created on Tue Dec 18 11:47:19 2018

@author: 612436198
"""

from random import randint

def diceGame():
    
    print("Welcome! I'm going to roll two dice and ask you to guess whether the sum of the two numbers rolled is odd or even.")
    
    guess = ""
    
    while type(guess) == str:
        
        dieOne = randint(1, 6)
        dieTwo = randint(1, 6)
        diceTotal = dieOne + dieTwo
    
        if diceTotal%2 == 0:
            rightAnswer = "even"
        else:
            rightAnswer = "odd"
    
        guess = input("Ok, dice rolled. Odd or even? If you don't want to play, type 'quit'.\n").lower()
        
        if guess == "quit":
            break

        elif guess == "odd" or guess == "even":

            secondGuess = input("The first die rolled a {}... would you like to change your mind (type 'y') or stick with your original guess (type 'n')?\n".format(dieOne))
    
            if secondGuess == "quit":
                break
            elif guess == rightAnswer and secondGuess == "n":
                print("Congratulations! The second die rolled a {}, making the sum {}. Well done for sticking to your guns.\nLet's play again.".format(dieTwo, diceTotal))
            
            elif guess != rightAnswer and secondGuess == "y":
                print("Congratulations! The second die rolled a {}, making the sum {}. Good second guessing.\nLet's play again.".format(dieTwo, diceTotal))
            elif guess == rightAnswer and secondGuess == "y":
                print("Argh, wrong! The second die rolled a {}, making the sum {}. First instincts can sometimes pay off.\nLet's play again.".format(dieTwo, diceTotal))
            elif guess != rightAnswer and secondGuess == "n":
                print("Argh, wrong! The second die rolled a {}, making the sum {}. Sometimes it pays to doubt yourself.\nLet's play again.".format(dieTwo, diceTotal))
            else:
                print("Not sure what happened there.\nLet's try again.")
        else:
            print("Whoops! Looks like there was a problem. Let's try again.")
    
    