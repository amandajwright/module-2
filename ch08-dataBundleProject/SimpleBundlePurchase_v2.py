# -*- coding: utf-8 -*-
"""
Created on Tue Dec 11 14:00:53 2018

@author: 612436198
"""

def DataBundlePurchase(truePasscode, balance):
    if passwordCheck(truePasscode):
        choice = transactionChoice()
        if choice == "1" and checkBalance(balance):
            return "Your balance is {}.".format(balance)
        elif choice == "1" and not checkBalance(balance):
            return "Your balance is not sufficient to purchase a data bundle: {}.".format(balance)
        else:
            if phoneNumberInput() == False:
                return "The numbers still don't match. Please try again later."
            else:
                transactionResultReason = transactionApproval(balance)
                if transactionResultReason == "balanceExceeded":
                    return "You have exceeded your balance."
                elif transactionResultReason == "maxAmountExceeded":
                    return "You have exceed the maximum amount."
                elif transactionResultReason == "multipleOfFiveFail":
                    return "The amount you entered is not divisible by five."
                else:
                    return str(transactionResultReason)
    else:
        return "Wrong password."
    
def passwordCheck(truePasscode):
    attempt = input("Please enter your password: ")
    if attempt == truePasscode:
        return True
    else:
        return False

def transactionChoice():
    choice = input("What would you like to do? To check your balance type 1, to purchase a data bundle type 2.\n")
    return choice

def checkBalance(balance):
    if balance > 0:
        return True
    else:
        return False

def phoneNumberInput():
    firstNumber = input("Please type your phone number: ")
    secondNumber = input("Please type your phone number again: ")
    if firstNumber == secondNumber:
        return (True, secondNumber)
    else:
        print("Sorry, the numbers don't match.")
        firstNumber = input("Please type your phone number: ")
        secondNumber = input("Please type your phone number again: ")
        if firstNumber == secondNumber:
            return (True, secondNumber)
        else:
            return False
        
def dataBundleTransaction():
    print("The maximum amount you can spend on data in one go is £100.")
    dataAmountRequested = float(input("How much would you like to spend today?\n£"))
    return dataAmountRequested

def transactionApproval(balance):
    dataAmountRequested = dataBundleTransaction()
    if dataAmountRequested > balance:
        transactionResultReason = "balanceExceeded"
    elif dataAmountRequested > 100:
        transactionResultReason = "maxAmountExceeded"
    elif dataAmountRequested%5 != 0:
        transactionResultReason = "multipleOfFiveFail"
    else:
        amountRemaining = round((balance - dataAmountRequested), 2)
        transactionResultReason = "Thank you for your purchase. Your remaining balance is £{}.".format(amountRemaining)
    return transactionResultReason
    