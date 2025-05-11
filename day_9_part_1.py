"""Write a loop that prompts the user to enter a series of 
pizza toppings until they enter a 'quit' value. As they enter each topping, 
print a message saying you’ll add that topping to their pizza."""
import os
os.system('cls')
toppings = []
while True:
    topping = input("Enter a pizza topping (or 'quit' to finish): ").strip().lower()
    if topping == 'quit':
        print("Finished adding toppings.")
        print(f"You have a beautiful pizza with the following toppings:{toppings}")
        break
    elif topping:
        toppings.append(topping)
        print(f"Adding {topping} to the pizza!")
        print("you have added following toppings:")
        for i in toppings:
            print(i)
    
    