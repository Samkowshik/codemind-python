s=input()
x=''
for i in s:
    if i.isalpha():
        x+=i
x=list(sorted(x))
s=list(s)
for i in range(len(s)):
    if s[i].isalpha():
        s[i]=x[0]
        x.pop(0)
print(''.join(s))