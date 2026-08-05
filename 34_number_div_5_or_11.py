num = int(input("Enter the number: "))

if num%5==0 and num%11==0:
    print(num, 'divisible by 11 and 5')
else:
    print(num, 'not divisible by 11 and 5')