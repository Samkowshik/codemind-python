s=input()
l=len(s)
v=['a','e','i','o','u']
mc=0
for i in range(l):
    for j in range(l):
        if j>=i:
            s1=s[i:j+1]
            for k in s1:
                if k not in v:
                    break
            else:
                if len(s1)>mc:
                    mc=len(s1)
print(mc)