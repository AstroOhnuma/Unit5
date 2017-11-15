#Astro Ohnuma
#11/13/17
#middleword.py - ask for a list of words and prints out the middle one

words = input('Enter a list of words: ').split(' ')
if len(words)%2 == 0:
    print(words[len(words)/2-1],words[len(words)/2])
else:
    print(words[len(words)/2])
