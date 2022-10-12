n1=int(input())
n2=int(input())
for n in range (n1,n2):
    if n==1:
        continue
    f=0
    for i in range (2,n):
        if n%i==0:
            f=1
            break
    if f==0:
        print(n)