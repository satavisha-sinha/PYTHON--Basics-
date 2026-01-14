# WAP to divide two integers

for i in range (1,2):
    a=int(input("Enetr 1st no. : "))
    b=int(input("Enter 2nd no. : "))
    if b==0:
        print("Division by zero error!")
        break
    else:
        print("quotient = ",a/b)
print("Program over")