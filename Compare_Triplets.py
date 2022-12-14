l1=list(map(int,input().split()))
l2=list(map(int,input().split()))
c=c1=0
for i in range(len(l1)):
    if l1[i]>l2[i]:
        c+=1
    if l1[i]<l2[i]:
        c1+=1
print(c,c1)