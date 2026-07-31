num = int(input("Enter the number: "))
count = 0
for i in range(1, len(str(num))):
    digit = num%10 
    if digit == 0:
        count +=1
    num = num//10
if count > 0:
    print('duck number')
else:
    print('not duck number')