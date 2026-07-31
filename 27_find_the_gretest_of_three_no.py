num1 = int(input("Enter the number1: "))
num2 = int(input("Enter the number2: "))
num3 = int(input("Enter the number3: "))

if(num1>num2 and num1>num3):
    print(num1, 'is greatest')
elif(num2>num1 and num2>num3):
    print(num2, 'is greatest')
elif(num3>num1 and num3>num2):
    print(num3, 'is greatest')
else:
    print('print all number are equal')
