from tkinter import *
from tkinter.ttk import *
from random import *
from time import *

#scenarios

def lunch():
    global studentAccount, savingsAccount
    decision = input("Would you like to go for lunch? (Yes/No)")
    if decision == "Yes" or decision == "yes" or decision == "Y" or decision ==  "YES" or decision == "y":
        if studentAccount <= 15:
            answer = input("You might not have enough money for that, would you like to take them from your savings account? (Yes/No)")
            if answer == "Yes" or answer == "yes" or answer == "Y" or answer == "YES" or answer == "y":
                withdrawSavings()

        cost = 5 + round(uniform(0, 10), 2)
        studentAccount = studentAccount - cost
        print("You have spent ", cost, " on lunch")
        displayBalance()
    else:
        pass
            

def drinks():
    global studentAccount, savingsAccount
    decision = input("Would you like to have drinks? (Yes/No)")
    if decision == "Yes" or decision == "yes" or decision == "Y" or decision == "YES" or decision == "y":
        if studentAccount <= 100:
            answer = input("You might not have enough money for that, would you like to take them from your savings account? (Yes/No)")
            if answer == "Yes" or answer == "yes" or answer =="Y" or answer == "YES" or answer =="y":
                withdrawSavings()
            else:
                pass
        r = (round(uniform(1, 10), 3)) * 10
        print("You have spent ", round(r, 2) , " on drinks")
        studentAccount = studentAccount - r
        savingsAccount = savingsAccount
        displayBalance()  
    else:
        pass


def goingOut():
    global studentAccount, savingsAccount
    decision = input("Do you want to go out? (Yes/No)")
    if decision == "Yes" or decision == "yes" or decision == "Y" or decision == "YES" or decision == "y":
        if studentAccount <= 25:
            answer = input("You might not have enough money for that, would you like to take them from your savings account? (Yes/No)")
            if answer == "Yes" or answer == "yes" or answer == "Y" or answer == "YES" or answer == "y":
                withdrawSavings()
            else:
                pass
                
        decision = input("Which club would you like to go to? (Subway / Why Not / Liquid Room) ")

        if decision == "Subway" or decision == "subway" or decision == "SUBWAY":
            additional_cost = round(uniform(0, 10), 2) + 10  # Random floating cost  # Deduct both fixed and random cost
            print("You have spent " , additional_cost + 10 , " on going out")

        elif decision == "Why Not" or decision == "why not" or decision == "WHY NOT":
            additional_cost = round(uniform(0, 15), 2)  # Random floating cost# Deduct both fixed and random cost
            print("You have spent " , additional_cost + 10 , " on going out")

        elif decision == "Liquid Room" or decision == "liquid room" or decision == "LIQUID ROOM":
            additional_cost = round(uniform(0, 12), 2)  # Random floating cost  # Deduct both fixed and random cost
            print("You have spent " , additional_cost + 10 , " on going out")
        
        studentAccount = studentAccount - additional_cost - 10
        displayBalance()
    if decision == "no" or decision == "No" or decision == "NO" or decision == "n" or decision == "N":
        pass
        

def groceries():
    global studentAccount, savingsAccount
    decision = input("Would you like to buy groceries? (Yes/No)")
    if decision == "Yes" or decision == "yes" or decision =="Y" or decision=="YES" or decision =="y":
        if studentAccount <= 30:
            answer = input("You might not have enough money for that, would you like to take them from your savings account? (Yes/No)")
            if answer == "Yes" or answer =="yes" or answer== "Y" or answer=="YES" or answer =="y" :
                withdrawSavings()
        sk = round(uniform(0, 30), 2) 
        print("You have spent " , sk, " on groceries")
        studentAccount = studentAccount - sk
        savingsAccount = savingsAccount
        displayBalance()
    else:
        pass    


def payRent(): #get rid of a fixed amount of money from student account 
    global studentAccount, savingsAccount
    print("It's the first of the month! Time to pay rent.")
    sleep(1.5)
    print("£600 will be automatically deducted from your account")
    studentAccount = studentAccount - 600
    decision = input("Would you like to save money?")
    if decision == "yes" or decision == "Yes" or decision == "Y" or decision == "y":
        depositSavings()
    else:
        pass
    sleep(1)
    return studentAccount

def impulsiveSpending():
    global studentAccount, savingsAccount
    u = randint(1,4)
    if u == 1:
        u = "snacks"
    elif u == 2:
        u = "sweat treat"
    elif u == 3:
        u = "coffee"
    else:
        u = "clothes"
    t = round(uniform(1,30), 2) 
    print("You have spent ", t , " on ", u)
    studentAccount = studentAccount - t
    displayBalance()


def displayBalance(): #updates account after purchase 
    global studentAccount, savingsAccount
    print("The balance of your student account is: £" , round(studentAccount , 2))
    print("The balance of your savings account is: £" , round(savingsAccount, 2))
    overdraft()
    newmoney = studentAccount
    return newmoney
    

def overdraft():
    global studentAccount, savingsAccount
    if studentAccount < -30:
        endGame()
    
    
def withdrawSavings(): #withdraw from savings account into student account 
    global studentAccount, savingsAccount
    withdraw = int(input("How much money do you want to withdraw?:"))
    while savingsAccount < withdraw:
            print("You do not have enough money in your account. Please choose a different amount of money to withdraw.")
            withdrawSavings()
    else:
        savingsAccount = savingsAccount - withdraw
        studentAccount = studentAccount + withdraw

def depositSavings(): #takes money from your account 
    global studentAccount, savingsAccount
    deposit = int(input("How much do you want to put into your savings?:")) 
    savingsAccount = savingsAccount + deposit 
    studentAccount = studentAccount - deposit 


#scenario functions

def scenarios():
    global studentAccount, savingsAccount
    y = randint(1,5)
    if y == 1 : lunch()
        
    if y == 2 : drinks()

    if y == 3 : goingOut()

    if y == 4 : groceries()
        
    if y == 5 : impulsiveSpending()

#game progression functions 

def endGame():
    global go
    print("You are bankrupt, and have therefore lost the game :(")
    go = False
    # import pdb; pdb.set_trace()

def days():
    global studentAccount, savingsAccount
    global day
    day += 1
    print("It is Day ", day)
    sleep(1.5)
    if day > 29:
        day = 0
        studentAccount += 240 
        print(f"Start of a new month! Your current student account balance is £{studentAccount} and your savings is £{savingsAccount}")
    displayBalance()



go = True
day = 1

#main game loop


studentAccount = 840
savingsAccount = 0
counter = 0
print("Welcome to Pocket Planner!")
sleep(1.5)
print("This game will simulate a month as a student.")
sleep(1.5)
print("You will be faced with different scenarios and decisions to make.")
sleep(1.5)
print("The aim of the game is to be as financially responsible as possible and not to get bankrupt.")
sleep(1.5)
print("You will be given a student account with a loan of £840 and a personal savings account.")
sleep(1.5)
print("Spend your money wisely and have fun!")
sleep(1.5)
k = payRent()
studentAccount = k
u = displayBalance()
sleep(2)
while go:
    if choice([True,False]):
        scenarios()
        counter =+ 1

        if go and counter < 3:
            if choice([True, False]):
                days()
                depositSavings()
                
            days()
            depositSavings()

    

     
