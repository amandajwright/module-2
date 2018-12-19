# -*- coding: utf-8 -*-


def DataBundlePurchase(truePasscode, balance):
    if passwordCheck(truePasscode):
        return transactionChoice(balance)
    else:
        print("Sorry, you have not entered a password that matches our records. Please check and try again later.")
        return "Transaction terminated due to incorrect password."
    
def passwordCheck(truePasscode):
    attempt = input("Please enter your password: ")
    if attempt == truePasscode:
        return True
    else:
        secondAttempt = input("Sorry, that does not match our records. Please enter your password (you have two attempts left): ")
        if secondAttempt == truePasscode:
            return True
        else:
            thirdAttempt = input("Sorry, that does not match our records. Please enter your password (you have one attempt left): ")
            if thirdAttempt == truePasscode:
                return True
            else:
                return False

def transactionChoice(balance):
    
    choice = input("Thank you. What would you like to do? To check your balance type 1, to purchase a data bundle type 2.\n")
    
    if choice == "1" and checkBalance(balance):
        print("Your balance is {}.".format(balance))
        return nextAction(balance)
    
    elif choice == "1" and not checkBalance(balance):
        print("Your balance is {}. As it is negative, you will be unable to carry out any further account activity today.".format(balance))
        return 'Customer informed of negative balance.'
    
    elif choice == "2":
        if phoneNumberInput() == False:
            print("The numbers still don't match. Please try again later.")
            return "Transaction terminated due to mismatching phone numbers."
        else:
            return transactionResponse(balance)
    
    else:
        print("There seems to be a problem. Please try again later.")
        return "Transaction terminated due to input of nonexistent choice."

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
        print("\nSorry, the numbers don't match.")
        firstNumber = input("Please type your phone number: ")
        secondNumber = input("Please type your phone number again: ")
        if firstNumber == secondNumber:
            return True
        else:
            return False
        
def dataBundleTransaction():
    print("\nThe maximum amount you can spend on data in one go is £100 and data is sold in amounts that are multiples of five.")
    dataAmountRequested = float(input("How much would you like to buy today?\n£"))
    return dataAmountRequested

def transactionApproval(balance):
    dataAmountRequested = dataBundleTransaction()
    if dataAmountRequested < 0:
        transactionResultReason = "negativeAmount"
    elif dataAmountRequested > balance:
        transactionResultReason = "balanceExceeded"
    elif dataAmountRequested > 100:
        transactionResultReason = "maxAmountExceeded"
    elif dataAmountRequested%5 != 0:
        transactionResultReason = "multipleOfFiveFail"
    else:
        amountRemaining = round((balance - dataAmountRequested), 2)
        print("Thank you for your purchase. Your remaining balance is £{}. Have a good day.".format(amountRemaining))
        transactionResultReason = "successfulTransaction"
    return transactionResultReason

def nextAction(balance):
    
    nextAction = input("Thank you. What would you like to do next? Type 1 for purchase data bundle or 2 for exit. ")
    
    if nextAction == "1":
        if phoneNumberInput() == False:
            print("The numbers still don't match. Please try again later.")
            return "Transaction terminated due to mismatching phone numbers."
        else:
            return transactionResponse(balance)
    
    elif nextAction == "2":
        print("Thank you. Hope to see you again soon.")
        return "Transaction terminated by customer's choice." 
    
    else:
        print("Sorry there seems to be a problem, please try again later.")
        return "Transaction terminated due to nonexistent choice input."

def transactionResponse(balance):
    
    transactionResultReason = transactionApproval(balance)
    
    if transactionResultReason == "negativeAmount":
        print("The amount you entered was a negative amount. Please try again.")
        return "Transaction terminated due to a negative amount having been entered."
    
    elif transactionResultReason == "balanceExceeded":
        print("The amount you entered exceeds your balance of £{}. Please try again".format(balance))
        return "Transaction terminated due to amount entered exceeding customer balance."
    
    elif transactionResultReason == "maxAmountExceeded":
        print("You have exceed the maximum amount of £100.")
        return "Transaction terminated due to amount entered exceeding maximum amount."
    
    elif transactionResultReason == "multipleOfFiveFail":
        print("The amount you entered is not divisible by five. Please try again.")
        return "Transaction terminated due to amount entered not being divisible by five."
    
    else:
        return str(transactionResultReason)
        