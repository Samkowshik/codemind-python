n=int(input())
print('0',end=' 1 ')
s1=0
s2=1
for i in range (1,n-1):
    s=s1+s2
    print(s,end=' ')
    s1=s2
    s2=s
