#Astro Ohnuma
#12/4/17
#quiz5.py - quiz on lists
from random import randint
#1
def rand5():
    randnums = [randint(1,100),randint(1,100),randint(1,100),randint(1,100),randint(1,100)]
    print(randnums)

rand5()
#2
def wordlengths(A):
   words = []
   words.append(A)
   for ch in words[0:]:
       print(words.count(ch))
wordlengths(['cat','dog','rat'])
#3
def lastelement(A):
    print(A[len(A)-1])
lastelement(['cat','dog','rat'])

