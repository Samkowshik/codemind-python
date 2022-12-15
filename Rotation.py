for t in range (int(input())):
    n,k=map(int,input().split())
    l=list(map(int,input().split()))
    if k==0 or k==n:
        print(*l)
        continue;
    if k>n:
        k=k%n
    a=l[n-k:]
    b=l[:n-k]
    print(*a,end=' ')
    print(*b)