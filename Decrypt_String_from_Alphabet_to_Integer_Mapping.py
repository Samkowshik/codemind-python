s=input()
while '#' in s:
    i=s.index('#')
    x=s[i-2:i+1]
    v=int(s[i-2:i])+96
    s=s.replace(x,chr(v))
for i in s:
    if i.isdigit():
        s=s.replace(i,chr(int(i)+96))
print(s)