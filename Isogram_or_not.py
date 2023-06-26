s=input()
d={}
for x in s:
    if x in d:
        print(False)
        break
    else:
        d[x]=1
else:
    print(True)