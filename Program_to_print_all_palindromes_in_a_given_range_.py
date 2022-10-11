def rev(n):
    s=0
    while n:
        r=n%10
        s=s*10+r
        n=n//10
    return s
n1=int(input())
n2=int(input())
for i in range (n1,n2+1):
    if i==rev(i):
        print(i,end=' ')