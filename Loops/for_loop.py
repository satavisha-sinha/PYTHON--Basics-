# WAP to multiply two integers without using the * operator using for loop

n1=int(input("Enter first no. :"))
n2=int(input("Enter second no. :"))
product=0
for i in range(n1):
    product+=n2
print("The product of these two numbers = ",product)

