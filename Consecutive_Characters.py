s=input()
ln=len(s)
mc=0
for i in range(ln):
    for j in range(ln):
        if j>=i:
            s1=s[i:j+1]
            l=len(set(s1))
            if l==1:
                if len(s1)>mc:
                    mc=len(s1)
print(mc)