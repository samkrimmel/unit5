#Sam Krimmel
#4/23/18
#middleWord.py - 

words = input('Enter a bunch of words: ').split(' ')

if len(words)%2 == 0:
    print(words[(len(words)//2)-1],words[(len(words)//2)])
else:
    print(words[(len(words)//2)])
