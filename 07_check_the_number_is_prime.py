# 7. Check whether a number is prime.

'''A prime number is a positive integer greater than 1 that has exactly two factors:

1
The number itself
×
×
×
100
4
2
2
25
5
5
100 factors into 2 × 2 × 5 × 5.
n
n
Learn more
Examples of Prime Numbers
Number	Factors	Prime?
2	1, 2	✅ Yes
3	1, 3	✅ Yes
4	1, 2, 4	❌ No
5	1, 5	✅ Yes
6	1, 2, 3, 6	❌ No
7	1, 7	✅ Yes
11	1, 11	✅ Yes
13	1, 13	✅ Yes'''

num = int(input("Enter the number: "))
count =0
for i in range(1, num+1):
    if(num%i==0):
        count +=1
if(count==2):
    print('prime number')
else:
    print('not prime number')