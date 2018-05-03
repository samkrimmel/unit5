#Sam Krimmel
#5/2/18
#cocktailSortDemo.py - implementing cocktail sort

from random import randint
from time import time

N = 10 #how many numbers will be sorted

def mySort(A,lo,hi):
    if lo < hi:
        p = partition(A,lo,hi)
        mySort(A,lo,p-1)
        mySort(A,p+1,hi)

def partition(A,lo,hi):
    pivot = A[hi]
    i = lo-1
    for j in range(lo,hi-1):
        if A[j] < pivot:
            i+= 1
            A[i], A[j] = A[j], A[i]
    A[i+1], A[hi] = A[hi], A[i+1]
    
    return i+1

if __name__ == '__main__':

    #make a list of N random numbers between 1 and N
    numbers = [0]*N
    for i in range(N):
        numbers[i] = randint(1,N)
    
    pythonSort = sorted(numbers) #Python's sort
    
    #time how long your sort takes
    t1 = time()
    numbers = mySort(numbers,numbers.min(),numbers.max())
    t2 = time()
    
    #print whether the sort worked or not
    try:
        assert(numbers == pythonSort)
        print('Your sort took', t2-t1, 'seconds')
    except:
        print('Your sort did not work')

