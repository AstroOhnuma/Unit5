#Astro Ohnuma
#11/17/17
#stat.py - takes a list of numbers and prints out the min, max, median, mean, and mode

numlist = []
print('Type a list of numbers')
print('Enter "q" when finished')

while True:
    numbers = input('>').sort([' '])
    if numbers == 'q':
        break