#Sam Krimmel
#4/25/18
#warmup15.py - Make a list of 20 random numbers between 1 and 100, print sum of list, min of list and max of list

from random import randint

numbers = []

for i in range(1,20):
    numbers.append(randint(1,100))

print(sum(numbers))
print(min(numbers))
print(max(numbers))
    