dd=int(input("Enter date:"))
mm=int(input("Enter month:"))
yyyy=int(input("Enter year:"))

print("Your date of birth is:",dd,"/",mm,"/",yyyy)

Cyear=int(input("Enter present year:"))
Cmonth=int(input("Enter present month:"))
Cday=int(input("Enter present date:"))

year=Cyear
month=Cmonth
day=Cday

month_days=[31,28,31,30,31,30,31,31,30,31,30,31]

if day<dd:
    month-=1
    day+=month_days[month-1]

if month<mm:
    year-=1
    month+=12

pday=day-dd
pmonth=month-mm
pyear=year-yyyy

print("You are",pday,"days,",pmonth,"months,",pyear,"years old.")


if month>mm:
    next_birthday_year=Cyear+1

elif month==mm and day>=dd:
    next_birthday_year=Cyear+1

else:
    next_birthday_year=Cyear

print("Your next birthday will be on:",dd,"/",mm,"/",next_birthday_year)