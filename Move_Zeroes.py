n=input()
l=list(map(int,input().split()))
c=0
for i in l:
    if i:
        print(i,end=' ')
    else:
        c+=1
if c:
    z=[0]*c
    print(*z)