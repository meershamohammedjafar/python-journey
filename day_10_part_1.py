"""Write a function called display_message() that prints one sen
tence telling everyone what you are learning about in this chapter. Call the 
function, and make sure the message displays correctly."""
import os
os.system('cls')
def dispplay_message():
    return "Im learning about writing functions"

print(dispplay_message())

"""Write a function called favorite_book() that accepts one 
parameter, title. The function should print a message, such as One of my 
favorite books is Alice in Wonderland. Call the function, making sure to 
include a book title as an argument in the function call"""

def favourite_book(book):
    return f"My favourite book is {book}"

print(favourite_book("The alchemist"))

"""8-3. T-Shirt: Write a function called make_shirt() that accepts a size and the 
text of a message that should be printed on the shirt. The function should print 
a sentence summarizing the size of the shirt and the message printed on it.
 Call the function once using positional arguments to make a shirt. Call the 
function a second time using keyword arguments."""

def make_shirt(size, text):
    return f"the size of the shirt is {size} and the message to be printed is {text}"

print(make_shirt(5,"You are braver than you think!"))
print(make_shirt(text="this is by using keyword argument!", size=5))

"""8-4. Large Shirts: Modify the make_shirt() function so that shirts are large 
by default with a message that reads I love Python. Make a large shirt and a 
medium shirt with the default message, and a shirt of any size with a different 
message."""

def make_shirt(size, text):
    if size == 'l' or size == 'L':
        print("i love python!")
    elif size == 'm' or size == 'M':
        print("i still love python")
    else:
        print(text)



input_size = input("enter size: ")
print(make_shirt(size = input_size, text = 'wassup'))
