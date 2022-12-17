s=input()
t=input()
while '#' in s:
    i=s.index('#')
    x=s[i-1:i+1]
    s=s.replace(x,'')
while '#' in t:
    i=t.index('#')
    x=t[i-1:i+1]
    t=t.replace(x,'')
print(s==t)