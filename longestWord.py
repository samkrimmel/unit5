#Sam Krimmel
#4/23/18
#longestWord.py - pritns the longest word of a list

words = input('Enter a list of words: ').split(' ')

longest = ' '
for word in words:
    if len(word) >= len(longest):
        longest = word
print(longest)
