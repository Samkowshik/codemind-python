n=int(input())
nu=list(map(int,input().split()))
n=int(input())
ind=list(map(int,input().split()))
l=[]
for i in range(n):
    l.insert(ind[i],nu[i])
print(*l)