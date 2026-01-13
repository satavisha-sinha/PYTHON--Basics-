# WAP to find the greatest number out of three numbers

a=int(input("Enter any no."))
b=int(input("Enter any no."))
c=int(input("Enter any no."))
if a>b and a>c :
    print(a,"is greater than",b,"and",c)
elif b>a and b>c :
    print(b,"is greater than",a,"and",c)
else:
    print(c,"is greater than",a,"and",b)
