'''An Armstrong Number (also called a Narcissistic Number) is a number that is equal to the sum of its own digits, where each digit is raised to the power of the total number of digits.

Formula

For a number with n digits:

Armstrong Number=d
1
n
	​

+d
2
n
	​

+d
3
n
	​

+⋯+d
n
n
	​


where d₁, d₂, ..., dₙ are the digits of the number.

Example 1: 153

Number = 153

It has 3 digits, so raise each digit to the power 3.

1³ + 5³ + 3³
= 1 + 125 + 27
= 153

Since the result is equal to the original number,

153 is an Armstrong Number. ✅'''


num = int(input("Enter the number: "))
arm_num = 0
temp = num
count = 0

for i in range(1,len(str(num))+1):
    count+=1

for j in range(1,len(str(num))+1):
    digit = num%10 #extract last digit
    arm_num = arm_num + digit**count
    num= num//10

if arm_num == temp:
    print(arm_num, "the number is armstrong")
else:
    print(arm_num, 'not a armstrong number')
