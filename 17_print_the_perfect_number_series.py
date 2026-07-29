s = int(input("Enter the start number: "))
e = int(input("Enter the end number: "))
for num in range(s,e+1):
    sum =0
    for i in range(1,num):
        if(num%i==0):
            sum = sum + i

    if(num==sum):
        print(num)
        