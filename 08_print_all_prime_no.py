n = int(input("Enter the number: "))

for num in range(2,n+1):
    count = 0
    for i in range(1,n+1):
        if(num%i==0):
            count +=1

    if(count==2):
        print(num)
    

