n=int(input())
l=list(map(int,input().split()))
lst=[0]*n
for i in range(n-1):
    l[i]=max(l[i+1:])
    print(l[i],end=' ')
print('-1')