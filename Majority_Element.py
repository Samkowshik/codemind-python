n=int(input())
l=list(map(int,input().split()))
d={}
for i in l:
    if i in d:
        d[i]+=1
    else:
        d[i]=1
m=max(d.values())
for k,v in d.items():
    if v==m:
        print(k)