# WAP to find the cube of an integer

count=1
while count>0:
    num=int(input("Enter the no. : "))
    if num==0:
        print("Oops you entered 0!\nPlease enter an integer")
        continue
    print("The cube of the given no. = ",num**3)
    count-=1