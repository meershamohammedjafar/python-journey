"""1. Echo With Types
Ask the user for anything with input().

Print the raw value.

Print type(raw_value).

Try converting the same value to int, then to float, printing each result and its type()."""

"""inp = input("Type in something: ")

print(inp)

print(f"Type of {inp}: {type(inp)} ")
print(f"{int(inp), {float(inp)}}")"""

"""2. Age in Months
Ask for age in years.

Convert the input to an integer.

Compute and print the age in months (years × 12).

"""

"""age = int(input("Age of your: "))
print(F"Age in month {age*12}")"""

"""3. Tip Calculator (Mini)
Ask for the bill total (float).

Ask for the tip percentage they’d like to leave (int, e.g., 10 for 10%).

Calculate the tip amount and print it rounded to two decimals."""

"""total_bill = float(input("total Bill: "))
tip_percent = int((input("Tip % youd like to leave: ")))
print(f"Tip to leave is: {total_bill/tip_percent}")"""

"""5. String ↔ Number Fails
Try each conversion and write down the exact error message:

python
Copy
Edit
int("ten")
float("12,5")
int("5.9")
Knowing common errors now will save hours later."""

"""print(int("A!$")) """
""": ValueError: invalid literal for int() with base 10: 'A!$'"""

"""6. Simple Grade Averager (Challenge)
Ask for three exam scores in one line separated by spaces (e.g., 80 75 92).

Split the string, convert each part to int, and compute the average.

Print:
"Your average is XX.X" (one decimal place)."""
marks = input("Enter three marks: ")
lst = marks.split()
print(marks)
print(lst)
for i in range(len(lst)+1, 1):
    print(lst[i])
    sum += lst[i]
    print(sum)
print(sum/len(lst))