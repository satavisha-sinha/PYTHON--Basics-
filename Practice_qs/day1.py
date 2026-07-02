# 1. WAP to calculate the electricity bill based on the
# following rules:
# Units <= 100 -- 2 rupees/unit
# Units 101-200 -- 3 rupees/unit
# Units >200 -- 5 rupees/unit
# INPUT: 150
# OUTPUT: Total electricity bill : 350

def find_bill():
    bill=0
    units=int(input("Enter the total units consumed : "))
    if units==0:
        print("Invalid input!")
    if units<=100:
        bill=units*2
    elif units>100 and units<=200:
        bill=((units-100)*3)+200
    elif units>200:
        bill=((units-200)*5)+500
    print("Total electricity bill : ",bill)

#-----------------------------------------------------

# 2. WAP to input three sides of a triangle of and check
# whether a triangle can be formed
# INPUT: 3
#        4
#        5
# OUTPUT: This is a valid triangle

def check_triangle():
    s1=int(input("Enter 1st side of the triangle :"))
    s2=int(input("Enter 2nd side of the triangle :"))
    s3=int(input("Enter 3rd side of the triangle :"))
    if s1==0 or s2==0 or s3==0:
        print("Invalid input!")
    elif (s1+s2>s3) and (s1+s3>s2) and (s2+s3>s1):
        print("This is a valid triangle")
    else:
        print("This is an invalid triangle")

#----------------------------------------------------------

# 3. WAP to input a single character and check whether it is :
# -Uppercase
# -Lowercase
# -Digit
# -Special character
# INPUT: A
# OUTPUT: Uppercase

def check_character():
    char=input("Enter a single character : ")
    if char.isupper():
        print("Uppercase")
    elif char.islower():
        print("Lowercase")
    elif char.isdigit():
        print("Digit")
    else:
        print("Special character")

#--------------------------------------------------------------

# 4. WAP to find the sum of all even numbers from 1 to n
# INPUT: 10
# OUTPUT: Sum of even numbers = 30

def sum_even_num():
    n=int(input("Enter number till you wamt to sum : "))
    lst=list(range(2,n+1,2))
    print("Sum of even numbers = ",sum(lst))

#--------------------------------------------------------------

# 5. WAP to count the number of digits in a given number
# INPUT: 4567
# OUTPUT: Number of digits = 4

def count_digit():
    numb=input("Enter any integer number : ")
    print("Number of digits = ",len(numb))

#--------------------------------------------------------------

# 6. WAP to reverse a given number
# INPUT: 1234
# OUTPUT: Reverse number = 4321

def rev_num():
    n=int(input("Enter any integer number : "))
    st=str(n)
    new=int(st[::-1])
    print("Reverse number = ",new)

    n=int(input("Enter any integer number : "))
    rev=0
    for i in range(len(str(n))):
        rev=(rev*10)+(n%10)
        n=n//10
    print("Reverse number = ",rev)

#--------------------------------------------------------------

# 7. WAP to check whether a given number is a palindrome.
# A palindrome number remains the same when reversed.
# INPUT: 121
# OUTPUT: Palidrome number

def check_palindrome():
    n=int(input("Enter the no you want to check : "))
    rev=0
    org=n
    for i in range(len(str(n))):
        rev=rev*10+(n%10)
        n=n//10
    if rev==org:
        print("Yes the number ",rev," is palindrome")
    else:
        print("No the number ",rev," is not palindrome")

# find_bill()
# check_triangle()
# check_character()
# sum_even_num()
# count_digit()
# rev_num()
# check_palindrome()
