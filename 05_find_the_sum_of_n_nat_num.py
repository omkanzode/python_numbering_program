# 5. Find the sum of first N natural numbers.

num =int(input("Enter the number: "))
sum = 0
for i in range(1,num+1):
    sum = sum + i
print('The sum of the number is: ', sum)