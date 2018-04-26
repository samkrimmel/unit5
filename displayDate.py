#Sam Krimmel
#4/25/18
#displayDate.py - displays current date

import datetime

today = datetime.date.today()

day = ['Mondey','Tueday','Wendsay','Thersday','Fridy']
month = ['January','February','March','April','May','June','July','August','September','October','November','December']

print("Todays date is", day[today.weekday()], month[today.month-1], str(today.day)+', '+ str(today.year))
