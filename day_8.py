import os

os.system('cls')  # Clear the console

library = {
    "alchemist": "Available",
    "book of magic": "Available",
    "book of potions": "Available",
}

user_input = input("Enter the name of the book you want to borrow: ").strip().lower()
print(user_input)

if user_input in library:
    if library[user_input] == "Available":
        print(f"you have borrowed the book '{user_input}'.")
        library[user_input] = "borrowed"
    else:
        print(f"Sorry the book '{user_input}' is already borrowed")
else:
    print(f"Sorry we don't have the book '{user_input}'")

print(library)