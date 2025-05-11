"""A movie theater charges different ticket prices depending on 
a person’s age. If a person is under the age of 3, the ticket is free; if they are 
between 3 and 12, the ticket is $10; and if they are over age 12, the ticket is 
$15. Write a loop in which you ask users their age, and then tell them the cost 
of their movie ticket"""

import os
os.system('cls')

counter = 0
number_of_tickets = int(input("How many tickets do you want to buy? : "))
while counter < number_of_tickets:
    counter+=1
    age = int(input("What is your age? : "))
    if age >= 3 and age < 12:
        print("Your ticket is free")
    elif age >= 12 and age < 15:
        print("Your ticket is $10")
    elif age >= 15:
        print("Your ticket is $15")
    else:
        print("You are not allowed to watch this movie")
        