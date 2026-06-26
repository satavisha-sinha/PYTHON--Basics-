# 1. print the multiplication table of a number

# num=int(input("Enter a number : "))
# for i in range(1,11):
#     print(i," x ",num," = ",i*num)

# 2. count the digits in a number

# n=int(input("Enter a number : "))
# dig=0
# if n==0:
#     dig=1
# else:
#     while n>0:
#         dig+=1
#         n=n//10
# print("Number of digits = ",dig)    

# 3. find the wheathe number if prime or not

import math
num=int(input("Enter a number : "))
prime= True
if num<=1:
    prime= False
else:  
    for i in range(2,int(math.sqrt(num))+1):
        if num%i==0:
            print("Not Prime")
            break
    else:
        print("Prime")

