# -*- coding: utf-8 -*-


#Task 1: Repeated division
x = 33
while x >= 1:
    print(x, ":", end=" ")
    x = x / 2
print(x) #exiting the while loop, when the condition is no longer True

#The 'end' above defines what separates what you're printing from the next thing that's going to print (the default is to print on a new line, the above says not on a new line, just after a space).

#Task 2: Computing triangular numbers
#pseudo-code for triangular number example:
#first you have a number, n
#you need to establish if n is greater than 0
#if it is, minus one from it and add it to itself, so n + (n - 1)
#reassign n - 1 as the new n
#add the new n to the result of the previous sum each time
#stop when n reaches zero

def triangular(n):
    trinum = 0
    while n > 0:
        trinum = trinum + n
        n = n - 1
    return trinum

triangular(1)
triangular(3)
triangular(5)

#Task 3: Student marks
mark = 1
while mark > 0:
    mark = int(input("What mark did you get? "))
    if mark >= 70:
        print("First class.")
    elif mark >= 40:
        print("Pass.")
    else:
        print("Fail.")

#same loop but with exit strategy:
didYouPass = 'Yes'

while didYouPass == 'Yes':
   mark = int(input('What is your score? '))
   if mark >= 70 and mark <=90:
       print('FIRST CLASS')
   elif mark >= 40:
       print('PASS')
   elif mark < 40:
       print('FAIL')
   didYouPass = input('Did you pass? ')
       
#Using break:
i = 55
while i > 10:
    print(i)
    i = 1 * 0.8
    if i == 35.2:
        break
A 'break' statement in a loop immediately terminates the current iteration and ends the loop overall. This can be very useful, for example when you just want to test part of a loop to evaluate results.
        
#Task 4: Using the break statement in a while loop
name = ""
while type(name) == str:
    name = input("Enter name: ").title()
    if name == "Done":
        break
    else:
        print("Hello {}!".format(name))

#Task 5: Guessing game
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
    
guess(3, 10)

#Task 6: Dice game
#from random import randint

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

diceGame()