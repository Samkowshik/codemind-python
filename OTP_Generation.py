s=input()
s1=''
for i in s:
    n=int(i)
    if n%2:
        n=n*n
        s1=s1+str(n)
print(s1)