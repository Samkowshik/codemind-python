n=input()
l=input().split()
l1=[len(x) for x in l]
m=max(l1)
l2=[int(l[i]) for i in range(len(l1)) if m==l1[i]]
print(*l2)