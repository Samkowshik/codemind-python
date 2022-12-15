n=int(input())
l=list(map(int,input().split()))
n=int(input())
for i in range(n):
    print(l[i],l[n+i],end=' ')