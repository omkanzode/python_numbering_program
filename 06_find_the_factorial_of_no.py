# 6. Find the factorial of a number.
'''A factorial of a number is the product of all positive integers from 1 up to that number.

It is represented by the symbol !.

Formula

For any positive integer n:

n!=n×(n−1)×(n−2)×⋯×2×1
Examples
1. Factorial of 5
5! = 5 × 4 × 3 × 2 × 1
   = 120'''


num = int(input("Enter the number: "))
fact = 1
for i in range(1, num+1):
    fact = fact*i
print(f"The factorial of {num} is {fact}")