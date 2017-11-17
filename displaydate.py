#Astro Ohnuma
#11/16/17
#displaydate.py - displays the current date
import datetime
today = datetime.date.today()
today.day
today.month
today.year
today.weekday()
month = ['January','February','March','April','May','June','July','August','September','October','November','December']
weekday = ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']
print('Today is',weekday[today.weekday()],',',month[today.month],today.day,today.year)