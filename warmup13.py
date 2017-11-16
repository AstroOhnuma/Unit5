#Astro Ohnuma
#11/16/17
#warmup13.py - make a list of random numbers
from random import randint
numbers = []

for i in range(1,20):
    nums = randint(1,100)
    numbers.append(nums)
print(numbers)
print(min(numbers))
print(max(numbers))
print(sum(numbers))
