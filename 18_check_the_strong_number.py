num = int(input("Enter your number: "))
temp = num
total = 0
for i in range(1, len(str(num))+1):
    digit = num%10
    fact = 1

    #find the factorial of the digit
    for j in range(1, digit+1):
       fact = fact*j

    total = total + fact
    num = num//10
print(total)
print(temp)
if(total==temp):
    print("This is strong number")
else:
    print("This is not strong number")
