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
print(L)
print('Min: ',min(L))
print('Max: ',max(L))
print('Mean: ',sum(L)/len(L))

if len(L)%2 == 0:
    print('Median: ', (L[len(L)//2] + L[(len(L)//2)-1])/2)
else:
    print('Median: ', L[len(L)//2])

mode = []
for i in range(0,len(L)):
    if L.count(L[i]) > mode:
        mode.append(L[i])


print('Mode: ',mode)

