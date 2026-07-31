num=int(input('enter the number: '))
sum=0
sq=num**2

while sq > 0:
    digit = sq % 10
    sum = sum + digit
    sq=sq//10

if sum== num:
    print('neon number')
else:
    print('not neon number')