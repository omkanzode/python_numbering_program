'''A Sunny Number is a number whose next number is a perfect square.

Definition

A number is called a Sunny Number if:

(number + 1) is a Perfect Square
Example 1: 8

Number:

8

Next number:

8 + 1 = 9

Since:

9 = 3 × 3

✅ 8 is a Sunny Number.'''

'''num = int(input("Enter the number: "))

l = []
for i in range(1, num+1):

    l.append(i**2)

if((num+1) in l):
    print("This is sunny number")
else:
    print("This is not sunny number")'''


num = int(input("Enter a number: "))

next_num = num + 1
flag = False

for i in range(1, next_num + 1):
    if i * i == next_num:
        flag = True
        break

if flag:
    print("Sunny Number")
else:
    print("Not a Sunny Number")
