num = int(input("Enter the number: "))
temp = num
rev = 0
for i in range(1, len(str(num))+1):
    digit = num%10
    rev = rev*10 + digit
    num//=10

print(f"The {temp} reverse number is {rev}")