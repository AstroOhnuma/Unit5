#Astro Ohnuma
#11/13/17
#wordsort.py - asks for a list of words, sorts them alphabetically, and then prints the list of words

words = input('Enter a list of words: ').split(' ')
words.sort()

for w in words:
    print(w)
