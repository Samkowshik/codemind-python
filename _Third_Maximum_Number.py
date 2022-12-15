n=int(input())
l=set(map(int,input().split()))
l=sorted(list(l))
if len(l)==1:
    print(l[0])
elif len(l)==2:
    print(l[1])
else:
    print(l[len(l)-3])