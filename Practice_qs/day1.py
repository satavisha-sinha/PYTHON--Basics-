# WAP to calculate the electricity bill based on the
# following rules:
# Units <= 100 -- 2rupees/unit
# Units 101-200 -- 3rupees/unit
# Units >200 -- 5rupees/unit
# INPUT: Total units consumed
# OUTPUT: Total electricity bill

# bill=0
# units=int(input("Enter the total units consumed : "))
# if units<=100:
#     bill=units*2
# elif units>100 and units<=200:
#     bill=((units-100)*3)+200
# elif units>200:
#     bill=((units-200)*5)+500
# print("Total electricity bill : ",bill)

#-----------------------------------------------------

# WAP to input three sides of a triangle of and check
# whether a triangle can be formed
# INPUT: Three integers for sides of the triangle
# OUTPUT: Print whether the triangle is valid or not

s1=int(input("Enter 1st side of the triangle :"))
s2=int(input("Enter 2nd side of the triangle :"))
s3=int(input("Enter 3rd side of the triangle :"))
if s1 or s2 or s3 ==0:
    print("Invalid input!")
elif s1+s2>s3:
    print("This is a valid triangle")
elif s1+s3>s2:
    print("This is a valid triangle")
elif s2+s3>s1:
    print("This is a valid triangle")
else:
    print("This is not a valid triangle")











