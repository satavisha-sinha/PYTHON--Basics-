a=int(input("Enter any no."))
b=int(input("Enter any no."))
c=int(input("Enter any no."))
min=mid=min=None
if a>b and a>c:
    if b>c:
        max,mid,min=a,b,c
    else:
        max,mid,min=a,c,b
elif b>c and b>a:
    if a>c:
        max,mid,min=b,a,c
    else:
        max,mid,min=b,c,a
else:
    if a>b:
        max,mid,min=c,a,b
    else:
        max,mid,min=c,b,a

print("Numbers in decending order : \n",max,"= MAX\n",mid,"= MID\n",min,"= MIN")

