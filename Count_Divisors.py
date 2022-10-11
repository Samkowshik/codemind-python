n1,n2,k=map(int,input().split())
c=0
for i in range (n1,n2+1):
    if i%k==0:
        c+=1
print(c)