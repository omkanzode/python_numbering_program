'''The question "Find the product of digits of a number" means:

Take each digit of the number and multiply them together.

The word product means multiplication.

Example 1

Number = 1234

Digits are:

1, 2, 3, 4

Multiply them:

1 × 2 × 3 × 4 = 24'''

num = int(input("Enter the number: "))

temp = num
fact = 1
for i in range(1, len(str(num))+1):
    digit = num%10
    fact = fact * digit
    num //=10
print(f'The product of the {temp} is {fact}')