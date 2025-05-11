"""Create a file called day3_numbers.py
Inside it:

Create a variable to store an integer age

Create another to store a float height

Use print() to display both."""

age = 22
height = 170.9

print(f"Meersha is of {age} age and of {height} height!")

"""Do Basic Math
Create two number variables (a, b) and:

Add, subtract, multiply, and divide them

Print each result clearly

Try with:

Only integers

One float + one int

Two floats"""

a, b = 5, 10

add = '{}+{}='.format(a, b)
sub = '{}-{}='.format(a, b)
mul = '{}*{}='.format(a, b)
div = '{}/{}='.format(a, b)

print(f'{add}',a+b,f'\n{sub}',a-b,f'\n{mul}',a*b,f'\n{div}',a/b)

"""Check Their Types
Use the type() function to print:

Type of 5, 5.0, "5"
Predict what will happen before you run it."""

a, b, c = 5, 5.0, '5'
print(type(a), type(b), type(c))

"""🔹 4. Try Casting Types
Convert:

A float to an integer (e.g. int(3.6))

An integer to a float

A string to a number (int("10"))

❌ Try converting "ten" to a number and observe the error. Record what the error says."""

#b is the float from previous code
casted = int(b)
print(type(b))

"""🔹 5. Challenge: BMI Calculator
Ask the user for:

Weight in kg (float)

Height in meters (float)

Then calculate BMI using:

BMI = weight / (height * height)

Print the BMI rounded to 2 decimal places.
🎯 Use round() function."""\

name = 'Meersha'
weight = 59.00
height = 170.90

bmi = weight/(height*height)
print(bmi)

print(f'BMI of {name} = {round(bmi, 3)}')