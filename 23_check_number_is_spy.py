'''A Spy Number is a number in which the sum of its digits is equal to the product of its digits.

Definition

A Spy Number is a number where:

Sum of Digits = Product of Digits
Example 1: 123

Digits:

1, 2, 3

Sum of digits:

1 + 2 + 3 = 6

Product of digits:

1 × 2 × 3 = 6

Since:

Sum = Product = 6

✅ 123 is a Spy Number.'''

num  = int(input("enter the number: "))
original = num 
temp = num 
sum = 0
fact = 1
for i in range(1,len(str(num))+1):
    digit = num%10 
    sum = sum + digit
    fact = fact * digit
    num = num//10

if(sum == fact):
    print("the number is spy")
else:
    print("The number is not spy")