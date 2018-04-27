#Sam Krimmel
#4/25/18
#stat.py

L = []
while True:
    num = input('Enter a list of numbers, enter q when finished: ')
    if num == 'q':
        break
    else:
        L.append(float(num))

L.sort()
print('Min: ',min(L))
print('Max: ',max(L))
print('Mean: ',sum(L)/len(L))
print('Median: ', L[len(L)//2]
print('Mode: ')
print(L)
