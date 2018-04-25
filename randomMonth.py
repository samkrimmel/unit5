#Sam Krimmel
#4/23/18
#randomMonth.py - prints out a random month of the year

from random import randint

months = ['January','February','March','April','May','June','July','August','September','October','November','December']

print(months[randint(1,12)-1])
