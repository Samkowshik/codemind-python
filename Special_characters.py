s=input()
c,l=0,[]
for i in s:
    d=i.isdigit()
    a=i.isalpha()
    if d:
        l.append(int(i))
    elif a:
        continue
    else:
        c+=1
l1=[i for i in l if i%2]
l2=[i for i in l if i%2==0]
s=''
if c%2:
    for i in range(min(len(l1),len(l2))):
        s=s+str(l1[i])+str(l2[i])
    if len(l2)>len(l1):
        t=l1
        l1=l2
        l2=t
    for i in range(i+1,len(l1)):
        s=s+str(l1[i])
    print(s)
else:
    for i in range(min(len(l1),len(l2))):
        s=s+str(l2[i])+str(l1[i])
    if len(l2)>len(l1):
        t=l1
        l1=l2
        l2=t
    for i in range(i+1,len(l1)):
        s=s+str(l1[i])
    print(s)