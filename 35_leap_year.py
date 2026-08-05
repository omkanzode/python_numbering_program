year = int(input("Enter the year: "))

if year%400==0:
    print(year)
elif year%4:
    print(year)
elif year%100:
    print(year,'not leap')
else:
    print(year,'not leap year')
