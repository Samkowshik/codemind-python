s=input()
s1=s
m=''
for i in range(len(s)):
    for j in range(i,len(s)):
        s1=s[i:j+1]
        s2=s1[::-1]
        if s1==s2 and len(s1)>len(m):
            m=s1
print(m)