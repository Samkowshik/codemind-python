s=input()
l=[int(i) for i in s if i.isdigit()]
m=10
for i in l:
    if i%2==0 and i<m:
        m=i
if m==10:
    print('-1')
else:
    l=list(set(l))
    l.remove(m)
    l.sort(reverse=True)
    s=''
    for i in l:
        s=s+str(i)
    print(s+str(m))