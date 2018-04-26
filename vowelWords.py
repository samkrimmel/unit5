#Sam Krimmel
#4/26/18
#vowelWordsDemo.py - how to treat strings as lists

words = input("Type in a goood ol' list of words: ").split(' ')

for thing in words:
    if thing[0] in 'aeiou':
        print(thing)

