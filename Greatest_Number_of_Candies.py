n=int(input())
l=list(map(int,input().split()))
k=int(input())
for i in l:
    i=i+k
    print(i>=max(l),end=' ')