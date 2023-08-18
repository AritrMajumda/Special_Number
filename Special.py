n=int(input("enter the number= "))
k=n
s=1
s1=0
q=0
while k>0:
    p=int(k%10)
    q=p+1
    for i in range(1,q):
        s=s*i
    s1=s1+s
    k=int(k/10)
    s=1
if(s1==n):
    print("special Number")
else:
    print("not special Number")