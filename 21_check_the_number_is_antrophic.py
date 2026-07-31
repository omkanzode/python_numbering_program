'''If the last digits of the square are the same as the original number, then it is called an Automorphic Number.

Example 1: 5

Number:

5

Square:

5 × 5 = 25

The square 25 ends with 5.

✅ 5 is an Automorphic Number.'''

num = int(input("Enter the number: "))
original = num 
sq = num**2

for i in range(len(str(sq))):
    digit = sq%10

    if(original==digit):
        print('auntrophic number')
        break
    else:
        print('not auntrophic number')

