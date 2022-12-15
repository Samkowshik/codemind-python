n=int(input())
l=list(map(int,input().split()))
l1=sorted(list(set(l)))
f=[l.count(i) for i in l1]
print(l1[f.index(max(f))])