num = int(input("Enter your number: "))
temp = num
count = 0
for i in range(1,len(str(num))+1):
    count +=1
    num = num//10
print(f"The {temp} of count digit present is {count}")