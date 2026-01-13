# WAP to multiply two integers without using the * operator using while loop

n1=int(input("Enter first no. :"))
n2=int(input("Enter second no. :"))
product=0
count=n1
while count>0:
    product+=n2
    count-=1
print("The product of these two numbers = ",product)
