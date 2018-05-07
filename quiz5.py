#Sam Krimmel
#5/7/18
#quiz5.py

def penultimate(L):
    return L[len(L)-2]

def plusEquals(numbers,num):
    for item in numbers:
        item += num
    return numbers
    
def smallest(numbers):
    smallest = sum(numbers)
    for item in numbers:
        if item < smallest:
            smallest = item
    return smallest

def decimalRange(first,last,step):
    L = []
    for i in range((last-first)/step):
        L.append(first+(step*i))
    return L
print(penultimate([3,4,5,6,7]))
print(plusEquals([1,2,3,4],10))
print(smallest([1,2,3,4]))
print(decimalRange(4,10,0.5))
