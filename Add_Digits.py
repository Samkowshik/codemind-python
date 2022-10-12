n=int(input())
while n//10!=0:
    d=n
    s=0
    while d!=0:
        r=d%10
        s=s+r
        d=d//10
    n=s
print(n)