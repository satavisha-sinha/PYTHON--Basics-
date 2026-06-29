def pyramid_stars():
    row=int(input("Enter the no of rows : "))
    for i in range(1,row+1):
        for j in range(1,row-i+1):
            print(" ",end=" ")
        for j in range(1,2*i):
            print("*",end=" ")
        for j in range(1,row-i+1):
            print(" ",end=" ")
        print()

def inverted_pyramid_stars():
    row=int(input("Enter the no of rows : "))
    for i in range(row,0,-1):
        for j in range(1,row-i+1):
            print(" ",end=" ")
        for j in range(1,2*i):
            print("*",end=" ")
        for j in range(1,row-i+1):
            print(" ",end=" ")
        print()

def side_pyramid_stars():
    row=int(input("Enter the no of rows : "))
    for i in range(1,2*row):
        if i<=row:
            for j in range(1,i+1):
                print("*",end=" ")
        else:
            for j in range(1,(2*row)-i+1):
                print("*",end=" ")
        print()


# pyramid_stars()
# inverted_pyramid_stars()
side_pyramid_stars()





