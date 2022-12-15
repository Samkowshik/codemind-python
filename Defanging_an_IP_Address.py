s=input()
while '.' in s:
    s1=s.replace('.','[.]')
    s=s.replace('.','')
print(s1)