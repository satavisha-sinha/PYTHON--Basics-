# Print a square with "*"

def sqr_stars():
    row=int(input("Enetr no. of rows you want : "))
    for i in range(row):
        for j in range(row):
            print("*",end=" ")
        print()

def rgt_tri_star():
    row=int(input("Enetr no. of rows you want : "))
    for i in range(row):
        for j in range(i):
            print("*",end=" ")
        print()


def rgt_tri_num():
    row=int(input("Enetr no. of rows you want : "))
    for i in range(1,row+1):
        for j in range(1,i+1):
            print(j,end=" ")
        print()


# sqr_stars()
# rgt_tri_star()
# rgt_tri_num()
