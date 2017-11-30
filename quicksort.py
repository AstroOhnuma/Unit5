#Astro Ohnuma
#11/30/17
#quicksort.py - implementation of quicksort

from random import randint
from time import time

N = 100 #how many numbers will be sorted
'''
algorithm quicksort(A, lo, hi) is
    if lo < hi then
        p := partition(A, lo, hi)
        quicksort(A, lo, p)
        quicksort(A, p + 1, hi)

algorithm partition(A, lo, hi) is
    pivot := A[lo]
    i := lo - 1
    j := hi + 1
    loop forever
        do
            i := i + 1
        while A[i] < pivot

        do
            j := j - 1
        while A[j] > pivot

        if i >= j then
            return j

        swap A[i] with A[j]'''

def quicksort(A):
        
if __name__ == '__main__':
    
    #make a list of N random numbers between 1 and N
    numbers = [0]*N
    for i in range(N):
        numbers[i] = randint(1,N)
        
    pythonSort = sorted(numbers) #Python's sort
    
    #time how long your sort takes
    t1 = time()
    numbers = quicksort(numbers)
    t2 = time()
       
    #print whether the sort worked or not
    try:
        assert(numbers == pythonSort)
        print('Your sort took', t2-t1, 'seconds')
    except:
        print('Your sort did not work')

