#Sam Krimmel
#5/2/18
#stoogeSort.py - implementing cocktail sort

from random import randint
from time import time

N = 200 #how many numbers will be sorted

def mySort(L,i,j):
    if L[i] > L[j]:
        L[i], L[j] = L[j], L[i]
    if (j-i+1) > 2:
        t = (j-i+1)//3
        mySort(L,i,j-t)
        mySort(L,i+t,j)
        mySort(L,i,j-t)
    return L

if __name__ == '__main__':

    #make a list of N random numbers between 1 and N
    numbers = [0]*N
    for i in range(N):
        numbers[i] = randint(1,N)
    
    pythonSort = sorted(numbers) #Python's sort
    
    #time how long your sort takes
    t1 = time()
    numbers = mySort(numbers,0,len(numbers)-1)
    t2 = time()
    
    #print whether the sort worked or not
    try:
        assert(numbers == pythonSort)
        print('Your sort took', t2-t1, 'seconds')
    except:
        print('Your sort did not work')

