# 2. Print numbers from 10 to 1.

num = int(input("Enter the number: "))

# for i in range(num, 0, -1):
#     print(i)

for i in range(-1,-(num+1),-1):
    print(i)