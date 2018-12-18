# -*- coding: utf-8 -*-
"""
Created on Tue Dec 18 11:29:42 2018

@author: 612436198
"""

from random import randint

def guess(attempts, range):
    
    number = randint(1, range)
    
    print("Welcome! Can you guess my secret number?")
    
    while attempts > 0:
        if attempts > 1:
            print("You have {} guesses remaining.".format(attempts))
        else:
            print("You have {} guess remaining.".format(attempts))
        attempts = attempts - 1
        guess = int(input("Make a guess: "))
        if guess == number:
            print("Yes! You guessed correctly, well done.")
            break
        elif guess > number:
            print("Nope, sorry: too high.")
        else:
            print("Nope, sorry: too low.")
    
    print("END-OF-GAME: thanks for playing!")