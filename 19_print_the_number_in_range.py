s = int(input("Enter the starting number: "))
e = int(input("Enter the ending number: "))

for num in range(s, e+1):
    
    orginal_num = num
    temp = num
    total = 0

    #extracting the last number 
    for i in range(1,len(str(num))+1):
        digit = temp%10

        #find factorial of the digit
        fact = 1
        for j in range(1, digit+1):
            fact = fact*j

        total = total + fact
        temp = temp//10


    
    if(total == orginal_num):
        print(orginal_num)

