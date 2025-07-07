print("💸TIP CALCULATOR")

print("1=Rs.")
print("2=Dollar")
print("3=Euro")
print("4=Dinar")
currency=int(input("Enter your Currency:"))

if currency==1:
    amount=float(input("Enter the Total Bill Amount:Rs."))
    
elif currency==2:
    amount=float(input("Enter the Total Bill Amount:$"))
    
elif currency==3:
    amount=float(input("Enter the Total Bill Amount:Euro"))
    
elif currency==4:
    amount=float(input("Enter the Total Bill Amount:Dinar"))
    
else:
    print("Please enter a valid Currency.")
    exit()
    
x=float(input("Enter the Tip Percentage you would like to give(%): "))

tip=(x*amount)/100
print("Tip Amount:",tip)

total=amount+tip
if currency==1:
    print("Total Amount:Rs.",total)
    
elif currency==2:
    print("Total Amount:$",total)
    
elif currency==3:
    print("Total Amount:Euro",total)
    
elif currency==4:
    print("Total Amount:Dinar",total)
    
else:
    print("Currency invalid.")
    exit()
    