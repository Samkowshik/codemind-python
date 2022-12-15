n,k=map(int,input().split())
l=list(map(int,input().split()))
if k>n:
    k=k%n
print(*l[k:],end=' ')
print(*l[:k])