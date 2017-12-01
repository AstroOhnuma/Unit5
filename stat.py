#Astro Ohnuma
#11/17/17
#stat.py - takes a list of numbers and prints out the min, max, median, mean, and mode

numlist = []
print('Type a list of numbers')
print('Enter "q" when finished')

while True:
    numbers = input('>')
    if numbers == 'q':
        break
    else:
        numlist.append(int(numbers))
print('Min: ',float(min(numlist)))
print('Mean: ',float(sum(numlist)/len(numlist)))
def median():
    if len(numlist)%2 == 0:
        print(numlist[len(numlist)/2-1],numlist[len(numlist)/2])
    else:
        print(numlist[len(numlist)/2])
print('Median: ',median())


