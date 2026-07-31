num1 = int(input("Enter the number1: "))
num2 = int(input("Enter the number2: "))

if(num1>num2):
    print(f"{num1} is greatest")
elif(num1==num2):
    print(f"{num1} is equal to {num2}")
else:
    print(f"{num2} is greatest")