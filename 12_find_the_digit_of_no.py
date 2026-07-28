'''
The question "Find the sum of digits of a number" means:

Take each digit of the number and add them together.

Example 1

Number = 1234

Digits are:

1, 2, 3, 4

Add them:

1 + 2 + 3 + 4 = 10

Answer = 10'''
num = int(input("Enter the number: "))
temp = num
sum = 0
for i in range(1, len(str(num))+1):
    digit = num%10
    sum = sum + digit
    num = num//10
print(f"The sum of {temp} is {sum}")