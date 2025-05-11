fruits = ['apple', 'bananna', 'cherry']
print(fruits)
fruits.append('orange') #appends t0 last element of the list
print(fruits)
fruits.insert(1, 'grape') #inserts at index 1
print(fruits)
fruits.remove('bananna') #removes the first occurrence of the value
print(fruits)
print(len(fruits))
fruits.sort() #sorts the list in ascending order
print(fruits)
fruits.reverse() #reverses the order of the list
print(fruits)

print(fruits[::-1])

for i in range(len(fruits)):
    print('using range function ',i+1,':',fruits[i])

for number, fruit in enumerate(fruits, start=1):
    print("using enumerate function ",number,':',fruit)


print(dir(tuple))
