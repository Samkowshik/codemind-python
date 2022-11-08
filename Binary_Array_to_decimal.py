n=int(input())
b=list(map(int,input().split()))
b.reverse()
i,s=0,0
for e in b:
    if e==1:
        s+=2**i
    i+=1
print(s)