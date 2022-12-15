n=int(input())
l=list(map(int,input().split()))
l=[i for i in l if l.count(i)==1]
if len(l):
    print(max(l))
else:
    print('-1')