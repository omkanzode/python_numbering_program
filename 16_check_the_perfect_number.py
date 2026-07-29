'''A Perfect Number is a positive integer that is equal to the sum of its proper divisors.

What are Proper Divisors?

Proper divisors are all the positive divisors of a number except the number itself.

Example 1: 6

Factors of 6:

1, 2, 3, 6

Proper divisors:

1, 2, 3

Sum of proper divisors:

1 + 2 + 3 = 6

Since the sum is equal to the original number,

6 is a Perfect Number. ✅'''

num = int(input("Enter the number: "))
sum = 0

for i in range(1, num):
    if(i%2==0):
        sum = sum + i
if(num==sum):
    print('perfect number')
else:
    print('not perfect number')