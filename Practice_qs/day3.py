# find the LCM  of any two numbers.

def lcm_hcf():
    num1=int(input("Enter the first number : "))
    num2=int(input("Enter the second number : "))
    lcm=max(num1,num2)
    maxn=lcm
    n1f=[]
    n2f=[]
    while True:
        if lcm%num1==0 and lcm%num2==0:
            break
        lcm+=1
    for i in range(1,maxn+1):
        if num1%i==0:
            n1f.append(i)
        if num2%i==0:
            n2f.append(i)
    cf=list(set(n1f) & set(n2f))
    hcf=max(cf)
    print("LCM : ",lcm)
    print("HCF : ",hcf)

lcm_hcf()