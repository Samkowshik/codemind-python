s=input()
v=['a','e','i','o','u']
ln=len(s)
ml=0
for i in range(ln):
    for j in range(i,ln):
        s1=s[i:j+1]
        l=len(s1)
        if l>ml:
            for k in s1:
                if k not in v:
                    break
            else:
                ml=l
print(ml)