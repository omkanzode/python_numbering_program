start = int(input("Enter the starting number: "))
end = int(input("Enter the ending number: "))
l = len(str(end))

for num in range(start,end+1):
    original = num 
    temp = num

    #count digits 
    count = 0 
    while temp>0:
        count+=1
        temp = temp//10

    temp = num # again store number of temp variable
    total = 0 

    # find sum of each digit raised to power 'count'

    while temp>0:
        digit = temp%10
        total = total + digit**count
        temp = temp//10

    if original ==total:
        print(num)
    