dd=int(input("Enter date:"))
mm=int(input("Enter month:"))
yyyy=int(input("Enter year:"))
print("Your date of birth is:",dd,"/",mm,"/",yyyy)
year=int(input("Enter present year:"))
month=int(input("Enter present month:"))
day=int(input("Enter present date:"))
pday=day-dd
if day<dd:
    pday=dd-day

else:
    pday=day-dd

pmonth=month-mm
if month<mm:
    pmonth=mm-month

else:
    pmonth=month-mm

pyear=year-yyyy
if year<yyyy:
    pyear=yyyy-year

else:
    pyear=year-yyyy

print("You are",pday,"days,",pmonth,"months,",pyear,"years old.")

age=year+1
print("Your next birthday will be on:",dd,"/",mm,"/",age)