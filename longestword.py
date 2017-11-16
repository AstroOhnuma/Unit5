#Astro Ohnuma
#11/15/17
#longestword.py - asks the user to for a list of words and then prints out the longest one

words = input('Enter a list of words: ').split(' ')
m = ' '
for w in words:
    if len(w)>len(m):
        m = w
print('The longest word is',m)

