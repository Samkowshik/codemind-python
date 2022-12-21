n=input()
l=input().split()
mc=c=0
for i in l:
    if i=='1':
        c+=1
        mc=c if c>mc else mc
    else:
        c=0
print(mc)