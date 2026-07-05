# 1. print the multiplication table of a number

def multiply_table(num):
    num=int(input("Enter a number : "))
    for i in range(1,11):
        print(i," x ",num," = ",i*num)

# 2. count the digits in a number

def count_digit(n):
    dig=0
    if n==0:
        dig=1
    else:
        while n>0:
            dig+=1
            n=n//10
    print("Number of digits = ",dig)


# 3. find the wheathe number if prime or not

import math
def find_prime():
    num=int(input("Enter no. to find prime or not : "))
    Prime=True
    if num<=1:
        Prime=False
    if  num%2==0:
        Prime=False
    else:  
        for i in range(2,int(math.sqrt(num))+1):
            if num%i==0:
                Prime=False
                break
        if Prime:
            print("Prime")
        else:
            print("Not Prime")

# multiply_table(3)
# count_digit(1234)
# find_prime()           