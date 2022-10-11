def rev(n):
    s=0
    while(n):
        r=n%10
        s=s*10+r
        n=n//10
    return s
n=int(input())
n+=rev(n)
while True:
    if n==rev(n):
        print(n)
        break
    else:
        n+=rev(n)