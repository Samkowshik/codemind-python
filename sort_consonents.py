s=input().split()
v=['a','e','i','o','u']
for i in range(len(s)):
    s1=list(s[i])
    x=''
    for j in s1:
        if j not in v:
            x+=j
    x=sorted(x)
    for j in range(len(s1)):
        if s1[j] not in v:
            s1[j]=x[0]
            x.pop(0)
    s[i]=''.join(s1)
print(' '.join(s))