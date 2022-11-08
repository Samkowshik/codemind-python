n=int(input())
b=list(map(int,input().split()))
i=0
for e in b:
    if e==1 or e==0:
        i+=1
if i==n:
    print(True)
else:
    print(False)