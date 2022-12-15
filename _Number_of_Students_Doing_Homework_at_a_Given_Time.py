n=input()
a=list(map(int,input().split()))
n=int(input())
b=list(map(int,input().split()))
k=int(input())
c=0
for i in range(n):
    if k>=a[i] and k<=b[i]:
        c+=1
print(c)