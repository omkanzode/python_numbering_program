# 3. Print even numbers from 1 to 100.

num =int(input("Enter the number: "))
for i in range(1,num+1):
    if (i%2==0):
        print(i)