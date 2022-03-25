print("Welcome to this Rock, Paper and Scissor Game>>>>>>>>>>>>>.") 
import time #to insert time module in python
X = input("Enter the name of first player>>>>>>>>") 
Y = input("Enter the name of second player>>>>>>>") 
time.sleep(2) #to hold 2 seconds between two extension
options = {"Rock","Paper", "Scissors"}
person_1 = input("Enter about your option %r" %X) 
person_2 = input("Enter your option %r" %Y)
if (person_1 == person_2): 
    print("Draw") 
    print("Noone wins the match>>>>") 
if (person_1 == "Rock" and person_2 == "Scissors"): 
    print("%r wins the match" %X) 
elif (person_1 == "Paper" and person_2 == "Rock"): 
    print("%r wins the match" %X) 
elif (person_1 == "Scissors" and person_2 == "Paper"): 
    print("%r wins the match" %X) 
elif (person_2 == "Rock" and person_1 == "Scissors"): 
    print("%r wins the match" % Y) 
elif (person_2 == "Paper" and person_1 == "Rock"): 
    print("%r wins the match" % Y) 
elif (person_2 == "Scissors" and person_1 == "Paper"): 
    print("%r wins the match" %Y)