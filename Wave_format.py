n=int(input())
lst=list(map(int,input().split()))
a=[0]*n
lst.sort(reverse=True)
j=0
for i in range(1,n,2):
    a[i]=lst[i-1]
if n%2:
    for i in range(0,n-1,2):
        a[i]=lst[i+1]
    a[-1]=min(lst)
else:
    for i in range(0,n,2):
        a[i]=lst[i+1]
print(*a)