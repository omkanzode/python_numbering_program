'''A Palindrome Number is a number that reads the same forward and backward.

Examples:
Number	Reverse	Palindrome?
121	     121	✅ Yes'''

num = int(input("Enter the number: "))
temp = num
rev = 0
for i in range(1, len(str(num))+1):
    digit = num%10
    rev = rev*10 + digit
    num = num//10
# print(rev)
# print(temp)
if(temp==rev):
    print('palindrom number')
else:
    print('not palindrom number')