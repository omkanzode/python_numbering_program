'''A Harshad Number (also called a Niven Number) is a number that is completely divisible by the sum of its digits.

Definition

A number is called a Harshad Number if:

Number % Sum of Digits == 0
Example 1: 18

Number:

18

Sum of digits:

1 + 8 = 9

Check divisibility:

18 % 9 = 0

✅ 18 is a Harshad Number.

Example 2: 21

Sum of digits:

2 + 1 = 3

Check:

21 % 3 = 0

✅ 21 is a Harshad Number.'''

num = int(input("Enter the number: "))
original = num
sum = 0
for i in range(1,len(str(num))+1):
    digit = num%10
    sum = sum + digit
    num = num//10
if(original%sum==0):
    print('This is harshad number')
else:
    print('This is not harshad number')
