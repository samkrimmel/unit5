#Sam Krimmel
#5/7/18
#quiz5.py

def penultimate(L):
    return L[len(L)-2]

def plusEquals(numbers,num):
    for i in range(0,len(numbers)):
        numbers[i] = numbers[i]+num
    return numbers
    
def smallest(numbers):
    smallest = sum(numbers)
    for item in numbers:
        if item < smallest:
            smallest = item
    return smallest
    
print(penultimate([3,4,4,120,20,6]))
print(plusEquals([1,21,31,4,1,1,0],15))
print(smallest([1,2,3,4,9,6,0,-5]))

