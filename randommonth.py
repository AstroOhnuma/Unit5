#Astro Ohnuma
#11/16/17
#randommonth.py - prints out a random month of the year
from random import randint

months = ['January','February','March','April','May','June','July','August','September','October','November','December']

month = randint(0,11)
print(months[month])
