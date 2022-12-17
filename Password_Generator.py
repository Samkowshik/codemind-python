s=input().split(',')
s1=''
for i in s:
    x,n=i.split(':')
    m=0
    for j in n:
        j=int(j)
        if j<=len(x) and j>m:
            m=j
    if m:
        s1=s1+str(x[m-1])
    else:
        s1=s1+'X'
print(s1)